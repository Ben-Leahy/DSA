from gusfields_z import z_algorithm
# from w2_lab import MatchedPrefix, Zsuffix
"""
Basic idea:
Right to left scanning of patten on text, then shifting the pattern to the right.
Bad Character Rule:
    - When we get a mismatch of a character, the bad character x is on the text. 
    - We can shift until we get to the next occurence of x in pattern. 
    - Create Bade Character Matrix
Good Suffix Rule:
 - When we get a partial match of the suffix of out pattern with the text
 - We can shift out pattern to the right until we find the next occurence of this suffix within pattern. 
 - We also want the next occurence of the suffix within the pattern to be good, 
    meaning that the preceeding character is different, meaning that it might actually be a match. 
Galil's optimisation:
    - Needed to guarantee linear time
    - Ensures that we don't re-compare letters. 

Iteratively:
    - Perform both bad character and good suffix rules using Galil's optimisation
    - Take maximum safe shift
    - Apply max safe shift
    

Data tables needed:
Bad Character Matrix 
    - This should be made using dynamic programming
    - DEF: a matrix stores for each letter, for each index, of the pattern, 
        the right most occurence to the left of that index of the bad character. 

Zsuffix List
    - This is needed to create Good Suffic Table
    - DEF: Zsuffix[i] stores the length of the longest substring of S ending at i that matches a suffix of S
        
Good Suffix List
    - This is needed to enact the main case of the Good Suffix Shift
    - We can calculate this by mapping Zsuffix (for proof see book)
    - DEF: The GS[i] stores the right most index of the right most occurence excluding the suffix, of the suffix S[i...m] where the previous char is different. 

Matched Prefix List
    - This is needed to find the largest safest shift when there is no occurence of the matched suffix of pattern occuring elsewhere in patter. 
    - In this case we need to search for a good prefix of this found suffix which occurs elsewhere. 
    - DEF: MP[i] stores the length of the largest suffix of S from S[i...N] that matches the prefix of S
"""

"""
Proofs
Case 2: When we find a match, shift by m - matched_prefix(1)
    # We draw an alpha box at the start and end of pattern, which is the length of matched_prefix(1). 
    # Then we imagine that there is some other occurence of alpha that exists rightwards of the prefix alpha. 
    # Well for this to be an issue, it has to match all the way to the start of the pattern. Because otherwise it will fail and not be a match
    # If it does this, then it would continue to the start of pattern, and be a prefix. 
    # If this was the case, then it would have to align with the suffix of the pattern of the same length:
        # because we found a match already, alpha continues to match the text. Because we are assuming we will find a match, prefix will match the pattern.
    # Hence prefix=suffix. This is a longer matched_prefix. But alpha was our longer matched prefix. Contradiction. 


"""

"""
Plan:
1. Set up functions Done
2. Code Boyer Moore assuming functions work Done
3. Code helper functions
3.5 Code speed ups - no comparing characters twice. 
3.6 Check function actually works :)

4. Set up functions for a1q1 
5. Code a1q1 assuming helper functions work
6. Code helper functions

7. Test
8. Ensure that the code can be run through command line with file names as inputs
"""

"""Code citing from online sources:
Code for taking arguments from command line: https://www.geeksforgeeks.org/python/command-line-arguments-in-python/ 
Code for declaring matrix without having issue with row's being dependent: https://www.geeksforgeeks.org/python/initialize-matrix-in-python/ 
"""

"""
Speed ups to consider:
- Let's not compare any two strings twice
- Can we store the bad char matrix differently? What about a dictionary at each location?
"""
import sys
def boyer_moore(txt: list[str], pattern: list[str]) -> list[int]:
    """|txt| = n, |pattern| = m
    Alphabet = {a, b, ..., z}, ascii range 97-122, https://www.ascii-code.com/characters/ascii-alphabet-characters

    Algorithm summary:
    # Left align text and pattern
        # Compare pattern with text right to left. 

    # If we match pattern:
        # Shift by m - matched_prefix(1)
    
    # If we don't pattern match:
        # shift max(bad_char_shift, good_suffix_shift)
        aabbabababbbbaabaabbabbaa
    """
    n, j = len(txt), 0 # length of text, iterator for txt
    m = len(pattern)
    matches = []

    # Preprocessing
    z_suffix = create_z_suffix(pattern)
    good_suffix = create_good_suffix(pattern, z_suffix)
    z = create_z_array(pattern)
    matched_prefix = create_matched_prefix(pattern, z)
    bad_char_matrix = create_bad_char_matrix(pattern)
    # While we have a valid alignment of pattern and text
    while j + m - 1 < n: # we index txt[j+i], max(txt[j+i]) = max(txt[j + m-1])
        shift = 0
        match_found = True
        mismatch_pos: int
        # Compare pattern with text
        for i in range(m - 1, -1, -1):
            if pattern[i] != txt[j + i]:
                match_found = False
                mismatch_pos = i
        if match_found:
            matches.append(j)
            shift = m - matched_prefix[1] # we know the m - matched_prefix(1) characters on the LHS will match
        else:
            shift = max(shift_bad_char(txt, mismatch_pos, bad_char_matrix), shift_good_suffix(m, good_suffix, matched_prefix, mismatch_pos))

        j += shift
    return matches
    
    
# ================ Define Reference Functions ===================
def shift_bad_char(txt: list[str], mismatch_pos: int, bad_char_matrix: list[list[int]]) -> int:
    bad_char = txt[mismatch_pos]
    shift = mismatch_pos - bad_char_matrix[mismatch_pos][index(bad_char)]
    return shift

def shift_good_suffix(m: int, good_suffix: list, matched_prefix: list, mismatch_pos: int) -> int:
    """
    # 1a we find a good suffix, shift by m-gs[k + 1]
    # 1b we don't, so we use matched_prefix
    """
    # 1a we find a good suffix
    if good_suffix[mismatch_pos + 1] > 0: # If mismatch_pos = right most char of pattern, then shift by 1. gs[-1] = m-1
        shift = m - good_suffix[mismatch_pos + 1]

    # 1b we don't, so we use matched_prefix. Proof by contradiction in notebook that this is valid. 
    else:
        shift = m - matched_prefix[mismatch_pos + 1]

    return shift

# ================ Create Reference Tables ===================
def create_matched_prefix(pattern: list[int], z: list[int]) -> list[int]:
    """DEF: matched_prefix[i] stores the length of the largest suffix of S from S[i...N] that matches the prefix of S"""
    """Start with z. """
    m = len(pattern)

    # Compute valid_suffix: valid_suffix[i] stores the length of the suffix[i...n-1] which matches the prefix. 
    # If there is not a suffix which matches the prefix, store 0. 
    valid_suffix = [0] * m 
    for i in range(m):
        if z[i] + i == m: # z value stores substring matching prefix. If z value is a suffix, then it goes in this array. 
            valid_suffix[i] = z[i]

    # Iterate over valid_suffix, and select largest from  S[i...N]
    matched_prefix = [0] * m
    max_suffix = 0
    for i in range(m-1, -1, -1):
        max_suffix = max(valid_suffix[i], max_suffix)
        matched_prefix[i] = max_suffix

    return matched_prefix

def create_good_suffix(pattern: list[str], z_suffix: list[int]) -> list[int]:
    """ 
    Definition: gs[i] stores the right most index, of the right most other occurence, of the suffix S[i...m] with a unique preceeding char. Otherwise 0
    Definition alt: gs[i] stores the right most other occurence of the suffix S[i...m], ending at i, with a unique preceeding char. Otherwise 0
    m = |pattern|
    gs(m-1 - z_suffix[i] + 1) = i""" # because end point is m-1, 0 based indexing
    m = len(pattern)
    gs = [0] * (m + 1)
    for i in range(m):
        gs[m - z_suffix[i]] = i
    gs[-1] = m - 1
    return gs

def create_bad_char_matrix(pattern: list) -> list[list[int]]:
    """
    O(|pattern| * |alphabet|) = O(m)
    """
    alphabet_size = 122 - 97
    m = len(pattern)
    matrix = [[-1] * alphabet_size for _ in range(m)] # -1 for 0 based indexing: when no occurence of bad_char is found, k-R(k,bad_char) = k + 1

    for i, char in enumerate(pattern): # TODO last iteration looks like what? I think I need to do  -1 on all the indexes and start from 1
        if i == m - 1:
            break
        # Carry previously found occurences. 
        for j in matrix[i]: # These are integers.
            matrix[i + 1][j] = matrix[i][j]
        # Update the rightmost occurence found to the left of index
        matrix[i + 1][index(char)] = i 
    return matrix

# ================ Helper Functions for preprocessing ================
def create_z_suffix(pattern: list[int]) -> list[int]:
    """ DEF: Zsuffix[i] stores the length of the longest substring of S ending at i that matches a suffix of S"""
    """Worst case is two linear reversals + z algo, O(n)"""
    z = create_z_array(reverse(pattern))
    return reverse(z)

def reverse(my_list: list) -> list:
    """Reverse function which returns a new list"""
    return my_list[::-1]

def create_z_array(s: str) -> list[int]:
    """z[i] store the length of the longest substring starting at i that matches the prefix"""
    # Define sample space
    n = len(s)
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    z = [n] + [0]*(len(s) - 1)
    l, r = -1, -1

    # Base case
    for i in range(0, n - 1):
        if s[i] == s[i + 1]:
            z[1] += 1
        else:
            break
    if z[1] > 0:
        l = 1
        r = z[1] 

    for k in range(2, n):
        # Case 1: k > r, naive pattern match
        if k > r:
            # print("case 1")
            for i in range(0, n - k):
                if s[i] == s[i + k]: 
                    z[k] += 1
                else:
                    break
            if z[k] > 0:
                r = k + z[k] - 1
                l = k

        # Case 2: k <= r
        else:
            # Case 2a:
            if z[k - l] < r - k + 1: 
                z[k] = z[k - l] 

            # Case 2b:
            elif z[k - l] > r - k + 1:
                z[k] = r - k + 1 

            # Case 2c: z[k-l] = r - k + 1:
            else: 
                z[k] = r - k + 1
                for i in range(0, n - 1 - r): 
                    if s[r - k + 1 + i] == s[r + i + 1]: 
                        z[k] += 1
                    else:
                        break
                l = k
                r = k + z[k] - 1
    return z

def index(char: str) -> int:
    """
    Alphabet = {a, b, ..., z}, ascii range 97-122
    ord('a') = 97, chr(97) = 'a'
    So when we create arrays which are length alphabet, we can just do: i = chr(x) - 97
    """
    return ord(char) - 97

# ================ Make file runnable ===================
if __name__ == '__main__':
    _, txt, pattern = sys.argv
    print(boyer_moore(list(txt), list(pattern)))
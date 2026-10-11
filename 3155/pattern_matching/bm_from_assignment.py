import sys
import os
import random
"""
Plan:
1. Set up functions Done
2. Code Boyer Moore assuming functions work Done
3. Code helper functions Done
3.5 Code speed ups - no comparing characters twice. Done
3.6 Check function actually works :) Done
3.6 TODO Galil's optimisation... why does it work even when we can't guarantee we don't compare characters twice for bad charf

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
# Worst case of a dictionary is O(n) where n is teh number if items in there... if we updated our create bad char matrix to an array of dictionaries we would have the same worst case with an imrpoved average case. 
ALPHABET_SIZE = 122 - 97 + 1
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
                mismatch_pos = i # mismatch position within pattern
                break # we only want the right most mismatch position.
        if match_found:
            matches.append(j + 1) # 1 based indexing.
            shift = m - matched_prefix[1] # we know the m - matched_prefix(1) characters on the LHS will match
        else:
            shift = max(shift_bad_char(txt, j, mismatch_pos, bad_char_matrix), shift_good_suffix(m, good_suffix, matched_prefix, mismatch_pos))

        j += shift
    return matches
    
    
# ================ Define Reference Functions ===================
def shift_bad_char(txt: list[str], j:int, mismatch_pos: int, bad_char_matrix: list[list[int]]) -> int:
    bad_char = txt[j + mismatch_pos]
    shift = mismatch_pos - bad_char_matrix[mismatch_pos][index(bad_char)]
    return shift

def shift_good_suffix(m: int, good_suffix: list, matched_prefix: list, mismatch_pos: int) -> int:
    """
    # 1a we find a good suffix, shift by m-gs[k + 1]
    # 1b we don't, so we use matched_prefix
    """
    # 1a we find a good suffix
    if good_suffix[mismatch_pos + 1] > 0: # If mismatch_pos = right most char of pattern, then shift by 1. gs[-1] = m-1
        shift = m - good_suffix[mismatch_pos]

    # 1b we don't, so we use matched_prefix. Proof by contradiction in notebook that this is valid. 
    else:
        shift = m - matched_prefix[mismatch_pos]

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
    DEF: a matrix stores for each letter, for each index, of the pattern, 
    the right most occurrence to the left of that index of the bad character. 
    DEF Alt: matrix[index][char] stores the right most occurrence of char to the left of index
    """
    m = len(pattern)
    matrix = [[-1] * ALPHABET_SIZE for _ in range(m)] # -1 for 0 based indexing: when no occurence of bad_char is found, k-R(k,bad_char) = k + 1

    for i, char in enumerate(pattern): # TODO last iteration looks like what? I think I need to do  -1 on all the indexes and start from 1
        if i == m - 1:
            break
        # Carry previously found occurences. 
        matrix[i + 1] = matrix[i].copy()
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

#==============================================================
# TESTING
#==============================================================
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # append 33862214 to sys path so that the import can find test_pattern_match
from test_pattern_match import test_search, test_search_multiple

def test_bm(txt_len: int = 100, pattern_len: int = 5) -> bool:
    return test_search(boyer_moore, txt_len, pattern_len)

def test_bm_multiple(test_count:int = 10) -> str:
    return test_search_multiple(boyer_moore, test_count)

# ================ Test Boyer Moore ===================
if __name__ == '__main__':
    print(test_bm_multiple())

# ================ Make file runnable from terminal ===================
# if __name__ == '__main__':
#     _, txt, pattern = sys.argv
#     print(boyer_moore(list(txt), list(pattern)))
#     print(naive_pattern_match(list(txt), list(pattern)))






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
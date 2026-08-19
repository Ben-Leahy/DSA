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



Pseudocode:
"""

def boyerMoore(pattern: list, txt: list) -> list:
    pass

def badCharMatrix(pattern: list) -> list[list[int]]:
    pass

def goodSuffixList(pattern: list, Zsuffix: list) -> list:
    """ Based on the logic and diagram we have on W2 Boyer Moore Good Suffix in notebook:
    m = |pattern|
    gs(m - Zsuffix[i] + 1) = i"""
    m = len(pattern)
    GS = [0] * m + [1]# Might need to check implication of 0 with regards to how it is used. Might need to default to m-1 or smth
    for i in range(m):
        GS[m - Zsuffix[i] + 1] = i
    GS[-1] = 1

def MatchedPrefix(s: list):
    """DEF: MP[i] stores the length of the largest suffix of S from S[i...N] that matches the prefix of S"""
    """Start with z. """
    # Z algo
    n = len(s)
    z = z_algorithm(s)

    # Filter by z values which are suffixes. 
    Zsuffix = [0] * n # This stores the length of the largest suffix of S at s[i] or 0 if no suffix
    for i in range(n):
        if z[i] + i == n:
            Zsuffix[i] = z[i] # This is now the longest suffixes that match the prefix. 

    # Use valid sufixes to find max suffixes from S[i...N]
    MP = [0] * n
    max_suffix = 0
    for i in range(n-1, -1, -1):
        max_suffix = max(Zsuffix[i], max_suffix)
        MP[i] = max_suffix

    return MP

def Zsuffix(S: list):
    """ DEF: Zsuffix[i] stores the length of the longest substring of S ending at i that matches a suffix of S"""
    """Worst case is two linear reversals + z algo, O(n)"""
    z = z_algorithm(S.reverse())
    return z.reverse()
#==============================================================
# HELPER FUNCTIONS
#==============================================================
# TODO I need to put in a unique terminal character... but how do I do this? what else will it break because I assume all characters are ascii 97-122?
# TODO my typehinting is wrong because they are expecting arrays atm. 
def create_suffix_matrix(txt: str) -> list[tuple[str, int]]:
    """returns a list of tuples, each containing a suffix and the index they start at with respect to txt"""
    txt = txt + '$'
    n = len(txt)
    doubled_txt = txt + txt
    suffixes = [] # list of tuples: (str, int)
    for i in range(n):
        tuple = (doubled_txt[i : i + n], i)
        suffixes.append(tuple)
    return suffixes

def create_sorted_suffix_matrix(txt: str) -> list[list[str]]:
    suffix_matrix = create_suffix_matrix(txt)
    suffix_matrix.sort(key = lambda tuple: tuple[0]) # '$' < 'a' already as is appears earlier in the ascii alphabet
    return suffix_matrix

def create_counts(bwt: list):
    """
    count[i] stores the number of occurrences of chr[i+97] in S. (Clearly alphabetically)

    Complexity: O(|Alphabet| * |bwt|)
    Storage: O(|Alphabet|)
    """
    ALPHABET_LENGTH = 122 - 97 + 1 
    counts = [0] * (ALPHABET_LENGTH + 1) # to include '$'
    for char in bwt:
        counts[index(char)] += 1
    # print(f'counts ({len(counts)}): ', counts)
    return counts
    
def index(char) -> int:
    """Assumes alphabet is ascii range 97 - 122, but includes '$' for terminal"""
    if char == '$':
        return 0
    else:
        return ord(char) - 97 + 1

#==============================================================
# REFERENCE TABLE CREATION
#==============================================================
def create_bwt_and_SA(txt: str) -> str:
    sorted_suffix_matrix = create_sorted_suffix_matrix(txt)
    sa = []
    bwt = ''
    for [suffix, i] in sorted_suffix_matrix:
        bwt += suffix[-1]
        sa.append(i)
    return bwt, sa

def create_rank(bwt: list, counts: list) -> list[int]: # TODO remove unecessary 
    """
    Rank[char] stores the index of the first occurrence of char in F: F = sorted(S), 
        or 0 if there are no occurrences. In this case, regardless of the value, ep < sp
    
    Complexity: O(|Alphabet| + |Alphabet| * |bwt|) = O(|Alphabet| * |bwt|)
    Storage: O(|Alphabet|) """
    rank = [0] * len(counts)
    max_rank = 0
    for i in range(0, len(counts)): 
        if counts[i] > 0: # 0 if no occurences
            rank[i] = max_rank
            max_rank += counts[i]
    # print(f'rank ({len(rank)}): ', rank)
    return rank

def create_n_occurrences(bwt: list[str]) -> list[int]:
    """
    noccurrences[i, char] stores the number of occurrences of char in BWT(S) from 1...i INCLUSIVE

    complexity: O(|Alphabet| * |bwt|)
    storage: O(|Alphabet| * |bwt|)
    """
    ALPHABET_LENGTH = 122 - 97 + 1 # including '$'
    n = len(bwt)
    matrix = [[0] * ALPHABET_LENGTH for _ in range(n)] # inner is alphabet

    for i, char in enumerate(bwt):
        if i > 0:
            matrix[i] = matrix[i - 1].copy() # TODO do I need to do this for BoyerMoore bad char array?
        matrix[i][index(char)] += 1
    # print('matrix', matrix)
    return matrix

def n_occurrences(char: str, i: int, occurrences: list[list[int]], inclusive: bool) -> int:
    """
    input:
        i: range, from 1...i that we are searching for char within bwt"""
    # Base case
    if i <= 0 and not inclusive:
        return 0
    else:
        if inclusive:
            return occurrences[i][index(char)]
        else:
            return occurrences[i - 1][index(char)]

#==============================================================
# PATTERN MATCHING
#==============================================================
def bwt_pattern_match(txt:str, pattern: list[str]) -> list[int]:
    """
    We assume ascii characters between 97 and 122
    :output: returns a list of all the indexes where the pattern begins
    """
    bwt, sa = create_bwt_and_SA(txt)
    n = len(bwt) # same as length of txt
    counts = create_counts(bwt)
    rank = create_rank(bwt, counts)
    occurrences = create_n_occurrences(bwt)

    sp = 0
    ep = n - 1
    for char in pattern[::-1]: # SERACH THE PATTERN IN REVERSE YOU DONKEY
        # print('-------------------------------')
        # print('sp: ', sp)
        # print('ep: ', ep)
        if sp > ep:
            return []
        else:
            # print('rank[index(char)]: ', rank[index(char)])
            # print('n_occurrences(char, sp, occurrences, inclusive=False); ', n_occurrences(char, sp, occurrences, inclusive=False))
            # print(' n_occurrences(char, ep, occurrences, inclusive=True) - 1: ',  n_occurrences(char, ep, occurrences, inclusive=True) - 1)
            sp = rank[index(char)] + n_occurrences(char, sp, occurrences, inclusive=False)
            ep = rank[index(char)] + n_occurrences(char, ep, occurrences, inclusive=True) - 1
    # sp and ep store with regards to bwt, so we want to convert this to the start indexes of S. 
    return sa[sp : ep + 1]


#==============================================================
# TESTING
#==============================================================
from test_pattern_match import construct_string, naive_pattern_match
def test_bwt(txt_len: int = 1000, pattern_len: int = 5) -> bool:
    txt = construct_string(txt_len)
    pattern = construct_string(pattern_len)
    bwt_matches = bwt_pattern_match(txt, pattern)
    bwt_matches.sort()
    if bwt_matches != naive_pattern_match(txt, pattern):
        print("------------------------------------------------------------")
        print(pattern)
        print(txt)
        print(bwt_matches)
        print(naive_pattern_match(txt, pattern))
        print("------------------------------------------------------------")
    return bwt_matches == naive_pattern_match(txt, pattern)

"""
Bug fixing issue
1. pattern matching wasn't working. 
    - resolve on this page
    - TODO resolve on boyer moore and ensure all testing suites point to the same
2. this now shows that bwt is not functioning as expected,
    - Confirm noccurrunces
1. we notice that our string generation generates a lot of stirngs which are all a's. 
2. our pattern matching doesn't work when it is all a's
3. the cases where the naive equals bwt is when both equal []. from increasing txt size we can see that this occurs when it shouldn't"""

def test_bwt_multiple(test_count:int = 100) -> str:
    successes = 0
    failures = 0
    for _ in range (test_count):
        if test_bwt():
            successes += 1
        else: 
            failures += 1
    return f"successes: {successes}  |  failures: {failures}"

if "__main__" == __name__:
    # pattern = 'aaaaa'
    # txt = 'aaaaabbaaaaaaaabaaaaaa'
    # print()
    # print(naive_pattern_match(txt, pattern))
    # ans = bwt_pattern_match(txt, pattern)
    # ans.sort()
    # print(ans)
    # txt = "banana"

    # bwt, sa = create_bwt_and_SA(txt)

    # print(bwt)
    # print(sa)

    # print(bwt_pattern_match("banana", "ana"))
    # print(bwt_pattern_match("banana", "nana"))
    # print(bwt_pattern_match("banana", "anab"))
    print(test_bwt_multiple())

#==============================================================
# APPLIED QUESTION CODE
#==============================================================
# We have done Q6 for BWT lab
def txt_from_bwt(bwt: list[str]) -> list[str]:
    pass

# Q4
# If we are doing inversion, then we only need an array for occurrences, 
# because at any index of BWT, we are only going to care about that character at that index. 
# So our array is just for each noccurrences[i] = BWT[0..i] of BWT[i]
#ie
def noccurrencesArrayForInversion(bwt, alphabet_size):
    count = [0] * alphabet_size
    n = len(bwt)
    noccurrences = [0] * n
    for i in range(n):
        char = bwt[i]
        noccurrences[i] = count[index(char)]
        count[index(char)] += 1


"""
BWT = L
Burrows wheeler transform of a text is:
    - create a matrix of all possible cyclic rotations of a txt
    - sort these cyclic rotations
    - take the last column

This is useful because we can match k patterns with h ocurrences of length m, from a text of length n in:
O(k*h*m + n)
ie we can preprocess the text once.

"""
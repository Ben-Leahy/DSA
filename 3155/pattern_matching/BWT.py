#==============================================================
# HELPER FUNCTIONS
#==============================================================
def create_suffix_matrix(txt: str) -> list[tuple[str, int]]:
    """returns a list of tuples, each containing a suffix and the index they start at with respect to txt"""
    n = len(txt)
    doubled_txt = txt + txt
    suffixes = [] # list of tuples: (str, int)
    for i in range(n):
        tuple = (doubled_txt[i : i + n], i)
        suffixes.append(tuple)
    return suffixes

def create_sorted_suffix_matrix(txt: str) -> list[list[str]]:
    suffix_matrix = create_suffix_matrix(txt)
    suffix_matrix.sort(key = lambda tuple: tuple[0])
    return suffix_matrix

def create_counts(bwt: list):
    """
    count[i] stores the number of occurences of chr[i+97] in S. (Clearly alphabetically)

    Complexity: O(|Alphabet| * |bwt|)
    Storage: O(|Alphabet|)
    """
    ALPHABET_LENGTH = 122-97
    counts = [0] * ALPHABET_LENGTH
    for char in bwt:
        counts[index(char)] += 1
    return counts
    
def index(char) -> int:
    """Assumes alphabet is ascii range 97 - 122"""
    return ord(char) - 97

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

def create_rank(bwt: list, counts: list) -> list[int]:
    """
    Rank[char] stores the index of the first occurence of char in F: F = sorted(S), 
        or 0 if there are no occurences. In this case, regardless of the value, ep < sp
    
    Complexity: O(|Alphabet| + |Alphabet| * |bwt|) = O(|Alphabet| * |bwt|)
    Storage: O(|Alphabet|) """
    max_rank = 0
    rank = [0] * len(counts)
    for i in range(1, len(counts)):
        if counts[i] > 0:
            rank[i] = max_rank + counts[i-1]
            max_rank = rank[i]
    return rank

def create_n_occurences(bwt: list[str]) -> list[int]:
    """
    nOccurences[char, i] stores the number of occurences of char in BWT(S) from 1...i INCLUSIVE

    complexity: O(|Alphabet| * |bwt|)
    storage: O(|Alphabet| * |bwt|)
    """
    ALPHABET_LENGTH = 122-97
    n = len(bwt)
    matrix = [[0] * ALPHABET_LENGTH for _ in range(n)] # inner is alphabet

    for i, char in enumerate(bwt):
        if i > 0:
            matrix[i] = matrix[i - 1]
        matrix[i][index(char)] += 1
    return matrix

def n_occurences(char: str, i: int, occurences: list[list[int]], inclusive: bool) -> int:
    """
    input:
        i: range, from 1...i that we are searching for char within bwt"""
    # Base case
    if i == 0 and not inclusive:
        return 0
    else:
        if inclusive:
            return occurences[i][index(char)]
        else:
            return occurences[i - 1][index(char)]

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
    occurences = create_n_occurences(bwt)

    sp = 0
    ep = n - 1
    for char in pattern:
        if sp >= ep:
            return []
        else:
            sp = rank[index(char)] + n_occurences(char, sp, occurences, inclusive=False)
            ep = rank[index(char)] + n_occurences(char, ep - 1, occurences, inclusive=True)
    # sp and ep store with regards to bwt, so we want to convert this to the start indexes of S. 
    return sa[sp : ep + 1]


#==============================================================
# TESTING
#==============================================================
from test_pattern_match import construct_string, naive_pattern_match
def test_bwt(txt_len: int = 5, pattern_len: int = 1000) -> bool:
    txt = construct_string(txt_len)
    pattern = construct_string(pattern_len)
    return bwt_pattern_match(txt, pattern) == naive_pattern_match(txt, pattern)

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
    print(test_bwt_multiple())

#==============================================================
# APPLIED QUESTION CODE
#==============================================================
# We have done Q6 for BWT lab
def txt_from_bwt(bwt: list[str]) -> list[str]:
    pass

# Q4
# If we are doing inversion, then we only need an array for occurences, 
# because at any index of BWT, we are only going to care about that character at that index. 
# So our array is just for each nOccurences[i] = BWT[0..i] of BWT[i]
#ie
def nOccurencesArrayForInversion(bwt, alphabet_size):
    count = [0] * alphabet_size
    n = len(bwt)
    nOccurences = [0] * n
    for i in range(n):
        char = bwt[i]
        nOccurences[i] = count[index(char)]
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
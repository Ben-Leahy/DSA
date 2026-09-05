# We have done Q6. 

# use ord() function

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

def create_bwt(txt: str) -> str:
    # Create matrix of suffixes
    n = len(txt)
    doubled_txt = txt + txt
    suffixes = []
    for i in range(n):
        suffixes.append(doubled_txt[i : i + n])

    # Sort matrix of suffixes
    suffixes.sort()
    
    # Take the last column and return
    bwt = ''
    for i in range(len(suffixes)):
        bwt += suffixes[i][-1]

    return bwt


def txt_from_bwt(bwt: list[str]) -> list[str]:
    pass

def pattern__match(bwt: list[str], pattern: list[str], rank: list[int]) -> list[str]:
    """
    We assume ascii characters between 97 and 122
    :output: returns a list of all the indexes where the pattern begins
    """
    m = len(pattern)
    n = len(bwt) # same as length of txt
    sp = 0
    ep = n - 1
    for i in range(m):
        sp = rank[ord(pattern[i])] + nOccurences[pat(i)] # TODO firstly, let's go back and actually make these data structures
        # we want to make them such that we can index based on the ord(char) - ASCII_RANGE, where ascii_range = 122-97
        # once we know this the pattern match is basically done. then we want to look at assignment again and compare 

    pass

def findCount(bwt: list):
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

def findRank(bwt: list, counts: list) -> list[int]:
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

def n_occurences(char: str, i: int, inclusive: bool, occurences: list[list[int]]) -> int:
    # Base case
    if i == 0 and not inclusive:
        return 0
    else:
        if inclusive:
            return occurences[index(char), i]
        else:
            return occurences[index(char), i - 1]


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

def nOccurences(bwt, alphabet)

if "__main__" == __name__:
    alphabet = ['$', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    bwt = ['o', 'o', 'o', 'l', 'o', 'o', 'o', 'o', 'o', 'l', 'w', 'm', 'l']
    counts = findCount(bwt, alphabet)
    print(counts)
    print(findRank(bwt, counts))
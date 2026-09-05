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
def create_bwt_and_SA(txt: str) -> str:
    # Create matrix of suffixes
    n = len(txt)
    doubled_txt = txt + txt
    suffixes = [] # list of tuples: (lst[str], int)
    for i in range(n):
        tuple = (doubled_txt[i : i + n], i)
        suffixes.append(tuple)

    # Sort matrix of suffixes
    suffixes.sort(key = lambda tuple: tuple[0])
    
    # Take the last column and return
    bwt = ''
    SA = []
    for i in range(len(suffixes)):
        bwt += suffixes[i][0][-1]
        SA.append(suffixes[i][1])

    return bwt, SA

def compare(tuple):
    return tuple[0]

def txt_from_bwt(bwt: list[str]) -> list[str]:
    pass

def pattern__match(bwt: list[str], SA: list[int], pattern: list[str], rank: list[int]) -> list[int]:
    """
    We assume ascii characters between 97 and 122
    :output: returns a list of all the indexes where the pattern begins
    """
    n = len(bwt) # same as length of txt
    sp = 0
    ep = n - 1
    counts = findCount(bwt)
    rank = findRank(bwt, counts)
    occurences = create_n_occurences(bwt)

    for char in pattern:
        if sp >= ep:
            return []
        else:
            sp = rank[index(char)] + n_occurences(char, sp, occurences, inclusive=False)
            ep = rank[index(char)] + n_occurences(char, ep - 1, occurences, inclusive=True)
    # sp and ep store with regards to bwt, so we want to convert this to the start indexes of S. 
    return SA[sp : ep + 1]

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

def n_occurences(char: str, i: int, occurences: list[list[int]], inclusive: bool) -> int:
    """
    input:
        i: range, from 1...i that we are searching for char within bwt"""
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
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

def pattern__match(bwt: list[str], pattern: list[str]) -> list[str]:
    """
    :output: returns a list of all the indexes where the pattern begins
    """
    pass

# What if I make a data structure that has alphabet, and rank. then at each index 
def count(bwt: list, alphabet):
    """Number of occurences of each letter in the alphabet"""
    # O(|Alphabet| * |bwt|)
    counts = [0] * len(alphabet)
    for char in bwt:
        j = findIndex(char, alphabet)
        counts[j] += 1
    return counts
    
def findIndex(char, alphabet) -> int:
    # TODO make this more efficient
    for i in range(len(alphabet)):
        if alphabet[i] == char:
            return i

def findRank(bwt: list, counts: list) -> list[int]:
    """O(|Alphabet| + |Alphabet| * |bwt|) = O(|Alphabet| * |bwt|)"""
    # TODO what should the rank be for letters that don't occur -> occurences will be 0, rank will be 0, then ep will -1. 
    max_rank = 0
    rank = [0] * len(counts)
    for i in range(1, len(counts)):
        # rank[i] = rank[i-1] + counts[i-1]
        if counts[i] > 0:
            rank[i] = max_rank + counts[i-1]
            max_rank = rank[i]
    return rank

def nOccurences(bwt: list) -> list[int]:
    # matrix for pattern matching
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
        nOccurences[i] = count[findIndex(char)]
        count[findIndex(char)] += 1

def nOccurences(bwt, alphabet)

if "__main__" == __name__:
    alphabet = ['$', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    bwt = ['o', 'o', 'o', 'l', 'o', 'o', 'o', 'o', 'o', 'l', 'w', 'm', 'l']
    counts = count(bwt, alphabet)
    print(counts)
    print(findRank(bwt, counts))
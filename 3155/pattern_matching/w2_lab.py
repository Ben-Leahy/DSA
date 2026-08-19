
from gusfields_z import z_algorithm
# This lab was applying gusfields z algorithm to a few use cases. 

# Q7
""" Write pseudocode for an algorithm that takes two strings S[1 . . . M] and
# T[1 . . . N] and returns the length of the longest suffix of S that exactly
# matches a prefix of T.
# ∗ What is the worst-case time complexity of your algorithm? """

# The z value is the length of the longest substring starting at i that matches the prefix. 
# We then want to filter these by genuine suffixes of S, not just substring. 
# T $ S, limit z algorithm to stop if it get's to an $. 
# Then if any Z value from S is: index + z value = |S| we have a valid suffix. 
def q7(S: list, T: list):
    """Worst case time complexity is O(n + m): it's just z algo on n and m + an iteration which is maximumally m
    We can't speed up z algo by just going it on m bc it relies on knowing previous z values (z[k-l])"""
    n = len(S)
    m = len(T)
    z = z_algorithm(S + '$' + T)
    longest_suffix_len = 0
    for i in range(n, n + m + 1):
        if z[i] + i == m:
            longest_suffix_len = z[i]
            break # if we find any value then we have already found the longest... they will only get shorter. 
    return longest_suffix_len

# Q8 =  Zsuffix
"""
8. Given a string S[1 . . . N], write pseudocode for an algorithm that computes an array
Zsuffix[1 . . . N], where each Zsuffix[i] stores the length
of the longest substring of S ending at position i that matches a suffix of S of the same length.
Reason the worst-case time complexity of your algorithm.
"""
# Okay, well our z array calculates the longest substring starting at i that matches the prefix
# So if we reverse the array. Then run Z. Then reverse Z, we get what we are after. 
def Zsuffix(S: list):
    """ DEF: Zsuffix[i] stores the length of the longest substring of S ending at i that matches a suffix of S"""
    """Worst case is two linear reversals + z algo, O(n)"""
    z = z_algorithm(S.reverse())
    return z.reverse()

# Q9
"""
Given a string S[1 . . . N], write pseudocode for an algorithm that computes an array MP[1 . . . N], where each MP[i] stores the length of the
largest suffix of the string S[i . . . N] that matches the prefix of S.
Reason the worst-case time complexity of your algorithm."""
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
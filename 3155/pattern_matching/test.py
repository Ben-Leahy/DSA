# Let's get our naive pattern matching to definitely work
def naive_pattern_match(txt: list[str], pattern: list[str]) -> list[int]:
    n = len(txt)
    m = len(pattern)
    matches = []
    for j in range(n - m + 1):
        match = True
        for i in range(m):
            if txt[j + i] != pattern[i]: #How has this never errored before???
                match = False
                # break
        if match:
            matches.append(j)
    return matches

pattern = 'aab'
txt = 'abbaabaab'
expect_output = [3, 6]
print(naive_pattern_match(txt, pattern))
# TODO my typehinting is wrong because they are expecting arrays atm. 
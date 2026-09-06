import random
# ================ Testing ===================
def construct_string(str_len: int):
    """
    Generate a string of length str_len which consists of a random alphabet size between 2 and 4, of which each letter in the alphabet has a random chance of being added to the list"""
    len_alphabet = round(random.randint(2, 4))
    possible_alphabet = ['a', 'b', 'c', 'd']
    alphabet = possible_alphabet[0:len_alphabet]

    spawn_chance = [random.random() for _ in range(0, len_alphabet)] 
    spawn_chance.sort()
    spawn_chance.append(1)

    string = ""
    while len(string) < str_len:
        x = random.random()
        for i in range(len(alphabet) - 1):
            if x < spawn_chance[i]:
                string += alphabet[i] # hold on because the last one doesn't get added. 
                break
    return string

def naive_pattern_match(txt: list[str], pattern: list[str]) -> list[int]:
    n = len(txt)
    m = len(pattern)
    matches = []
    for j in range(n - m + 1):
        match = True
        for i in range(m):
            if txt[i] != pattern[j + i]:
                match = False
            break
        if match:
            matches.append(j)
    return matches
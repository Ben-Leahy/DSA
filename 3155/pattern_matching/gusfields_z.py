import random

def z_algorithm(s: str) -> list[int]:

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

         
################################################################################
def naive_preprocessing(s: str) -> list[int]:
    # Define z of length len(s) initiated with 0
    z = [len(s)] + [0]*(len(s) - 1)
    for i in range(1, len(s)):
        for j in range(0, len(s)):
            if i + j < len(s) and s[j] == s[i + j]:
                z[i] += 1
            else:
                break

    return z

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

def test_z_once(str_len:int = 10000):
    print("#################################### single z test")
    s = construct_string(str_len)    
    z1 = naive_preprocessing(s)
    z2 = z_algorithm(s)

    print("Zn: " + str(z1))
    print("Zg: " + str(z2))
    print('s: ' + s)
    print(z1==z2)

def test_z_multiple():
    # TODO I should do this in parallel so that I can speeed up the naive version
    test_count = 5
    for _ in range(test_count):
        test_z_once(20) #Change after testing 
        # TODO why are they random length strings what the hell? My generation algo is fuked. 

def test():
    tests = ["bbabbbabbabbcbabcba", "aaaabbabaabbaabababaabbaababaaaaabbbababa", "abbcbabbcbcabbcbabcbabaabababbcbcabbabbbabbabbcbabcba", "bbbbbbbbbbbbbbbbbbbbb"]
    for test in tests:
        
        z1 = naive_preprocessing(test)
        z2 = z_algorithm(test)

        print("############################################ custom z test")
        print("test: " + test)
        print("Zn: " + str(z1))
        print("Zg: " + str(z2))
        print("Z matches naive: ", z1==z2)

if __name__ == '__main__':
    test()
    test_z_multiple()

    """
    #################################### single z test
Zn: [20, 5, 4, 3, 2, 1, 0, 6, 12, 5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1]
Zg: [20, 5, 4, 3, 2, 1, 0, 6, 8, 5, 4, 3, 2, 1, 0, 1, 4, 3, 2, 1]
s: bbbbbbabbbbbbbabbbbb
False
"""
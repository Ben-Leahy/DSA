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
            print("case 1")
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
            if z[k - l] < r - k + 1: # + 1 justification: consider z[k-l] = 1, and r-k = 1, this should be equal by diagram
                print("Case 2a")
                print("z: " + str(z) + '\n l: ' + str(l) + '\n r: ' + str(r) + '\n k: ' + str(k) + '\n')
                z[k] = z[k - l] # TODO this just doesn't look right when I'm coming back to it but I am not looking at the diagram.

            # Case 2b:
            elif z[k - l] > r - k + 1:
                print("Case 2b")
                print("z: " + str(z) + '\n l: ' + str(l) + '\n r: ' + str(r) + '\n k: ' + str(k) + '\n')
                # print(z)
                # print('l: ' + str(l))
                # print('r: ' + str(r))
                # print('k: ' + str(k) + '\n')
                z[k] = r - k + 1 
                # l=k # optional?

            # Case 2c: z[k-l] = r - k + 1:
            else: 
                print("Case 2c")
                print("z: " + str(z) + '\n l: ' + str(l) + '\n r: ' + str(r) + '\n k: ' + str(k) + '\n')
                # Iterate from end of prefix matched so far
                # for i in range(r - k, n - k):
                z[k] = r - k + 1
                for i in range(r - k + 1, n - r):
                    if s[i] == s[i + k]: # we alr know s[i + k] = s[r]
                        z[k] += 1
                    else:
                        break
                # If the substring matches a longer prefix update
                l = k
                r = k + z[k] - 1
    return z
            # This was the old one, the issue was that I had updating z[k] inside a conditional, however even if I don't increment it, it should still be r-k+1
            # # Case 2c: z[k-l] = r-l
            # else: 
            #     print("Case 2c")
            #     print("z: " + str(z) + '\n l: ' + str(l) + '\n r: ' + str(r) + '\n k: ' + str(k) + '\n')
            #     # Iterate from end of prefix matched so far
            #     # for i in range(r - k, n - k):
            #     # TODO surely the error is coming from here? But they all look right??
            #     for i in range(r - k + 1, n - r):
            #         if s[i] == s[i + k]: # we alr know s[i + k] = s[r]
            #             z[k] += 1
            #         else:
            #             break
            #     # If the substring matches a longer prefix update
            #     if z[k] > 0:
            #         z[k] += z[k-l]
            #         r = k + z[k]
            #         l = k
         
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
    spawn_chance = [random.random() for _ in range(0, len_alphabet)] #spawn_chance = [random.random() for _ in range(0, len_alphabet - 1)]
    spawn_chance.sort()

    string = ""
    while len(string) < str_len:
        x = random.random()

    #

    for i in range(0, str_len):
        x = random.random()
        for i in range(len(alphabet) - 1):
            if x < spawn_chance[i]:
                string += alphabet[i] # hold on because the last one doesn't get added. 
                break
        if len(string) < i:# add the last letter of the alphabet if it hasn't already been added. 
            string += alphabet[-1]


    return string

def test_z_once(str_len:int = 10000):
    print("####################################")
    s = construct_string(str_len)    
    z1 = naive_preprocessing(s)
    z2 = z_algorithm(s)

    print("Zn: " + str(z1))
    print("Zg: " + str(z2))
    print('s: ' + s)

def test_z_multiple():
    # TODO I should do this in parallel so that I can speeed up the naive version
    test_count = 10
    for _ in range(test_count):
        test_z_once(20) #Change after testing 
        # TODO why are they random length strings what the hell? My generation algo is fuked. 

def test():
    tests = ["bbabbbabbabbcbabcba", "aaaabbabaabbaabababaabbaababaaaaabbbababa", "abbcbabbcbcabbcbabcbabaabababbcbcabbabbbabbabbcbabcba"]
    for test in tests:
        
        z1 = naive_preprocessing(test)
        z2 = z_algorithm(test)

        print("############################################")
        print("test: " + test)
        print("Zn: " + str(z1))
        print("Zg: " + str(z2))
        print("Z matches naive: ", z1==z2)

if __name__ == '__main__':
    # z_algorithm("bbabbbabbabbcbabcba")
    test()

    # test_z_multiple()
    # print(z_algorithm('aaabaaababaabbaba'))
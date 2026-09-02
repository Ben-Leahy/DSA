def lempel_ziv(txt: str):
    MAX_SEARCH_WINDOW = 10
    MAX_LOOKAHEAD_BUFFER = 10
    sw = 0 # search window
    lb = MAX_LOOKAHEAD_BUFFER# lookahead buffer
    i = 0

    n = len(txt)
    for i in range(n):
        # Find maximum length between sw and lb

        # Okay instead to do this it's the sw*n, and we just prepend [i...lb+i] with [i-sw... i] and run z

    # longest substring from i to MAX_LOOKAHEAD_BUFFER that matches some string in sw to lb
    # use some data structure we have already learnt to do this. 
    # use the right most 
    #[offset, len, next char] is calciulated each time, but an array of length n of these arrays. 
        #offset = i - found index start
        # len = data_structure[found_index_start]
        # next char = txt[i + len]
    #output[i] = [offset, len, next char]

    # Then we need to encode this. 
    # fo ri in range (len(output))
        # for i in range (3):
            # elias, elias, huffman
    pass

def lempel_ziv_decoding():
    pass


def lzss():
    # [1, char] for length of less than 3
    # [0, offset, lenght] for length of 3 or more
    pass

def lzss_decoding():
    pass
def elias_omega():
    pass
    # find minimum binary encoding of the number. 
        # length = length of bit array

    # find binary encoding of length
        # Flip leading character to 0

    # Find the length of the previous length component until the new length is 1, ie the previous was 2
        # Flip leading character to 0

    
def elias_omega_decoding() -> int:
    """
    :inpput: Takes in bit array elias omega encoding of number
    :output: decimal of number"""
    pass
    #read the first bit
    # if 0, it is a length component. Flip leading to 0. Find decimal
    # Read next decimal numbers
    # if leading is 0, flip leading, find decimal, read next decimal numbers
    # If leading is 1, read the digits and convert to decimal

    # Wait what happens to rpresent numbers 0 and 1?
        # 0 we can't do this, it's just for integers. 
        # 1 is 1 -> 1
        # 2 is 10 -> 1 10 -> 010
    # I clearly don't understand becuase doesn't 0 mean 1 mean search 1 bit? It must mean +1. Otherwise we couldn't grow it. 
    
    # To map this to negative , 0 and positive integers, 
        # 0 -> 1
        # 1 -> 2
        # -1 -> 3

def min_bin_encoding(num: int): 
    # Something to do with remainders. 
    pass
# TODO figure out how to work with binary numbers


"""proof
Assume they are not uniquely encodable
We go until we are told to read the encoding and not the length
then somehow we stop before reading another encoding or the rest of the encoding? 
This is not possible"""
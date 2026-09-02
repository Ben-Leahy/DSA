"""
TODO:
    - Implement the min_binary_encoding
    - 
"""

def elias_omega_encoding(num: int):
    # TODO this could be recursive, would that be better? 

    # Base case
    if num == 1:
        return 1

    # Encode number (minimum binary encoding)
    bit_encoding = min_bin_encoding(num)
    length = len(bit_encoding)

    # Prepend length components: minimum binary encoding of previous segment-1
    while length > 1:
        length_component = flip_leading_bit(min_bin_encoding(length - 1))
        bit_encoding = length_component + bit_encoding
        length = len(length_component)

    return bit_encoding
    
def elias_omega_decoding(encoding: []) -> int:
    """
    :inpput: Takes in bit array elias omega encoding of number
    :output: decimal of number"""
    # Base case
    if encoding[0] == 1:
        return 1

    read_from = 0
    segment = read(1, read_from, encoding)

    while True:
        # If decode number
        if segment[0] == 1:
            return binary_to_int(segment)
        # Decode length component
        else:
            bin = flip_leading_bit(segment)
            length = binary_to_int(bin) + 1
            read_from += len(segment)
            segment = read(length, read_from, encoding)

def read(num, from_index : int, list:list[int]) -> list[int]:
    return []

def min_bin_encoding(num: int) -> list[int]: 
    return []

def binary_to_int(list:list[int]) -> int:
    return 0

def flip_leading_bit(d: list[int]):
    return []

"""proof
Assume they are not uniquely encodable
We go until we are told to read the encoding and not the length
then somehow we stop before reading another encoding or the rest of the encoding? 
This is not possible"""
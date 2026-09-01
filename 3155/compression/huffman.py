"""Reflectoin from class. Just follow the class and if there are other things ii want to investigate note them down and do them later."""
class Node:
    def __init__():
        #is leaf
        # freq?
        #edges []
        pass

class edge: 
    def __init__():
        pass
    # 1 or 0

def huffman(sorted_freqs: list[int]) -> list[int]: # -> Node
    """
    Construct a deterministic variable length encoding for characters. 
    This is necessary to compress - we can store more common examples with shorter characters. 
    This needs to be prefix free to go in both directions
    The basic idea is to store each encoding as a path to a leaf in a strict binary tree. This way no leaf is a prefix of another leaf.
    This generates the decoding graph.
    :output: root node of the graph"""
    pass
    # While sorted_freqs length >= 2:
        # Select top 2, sorted_freqs[0], sorted_freqs[1]
        # Create a new node that points to them: 0 to the one with the lower freq, with freq= sorted_freqs[0] + sorted_freqs[1]
        # Also have a pointer to root which is updated to a new node each time. 
        # Remove sorted_freqs[0], sorted_freqs[1] from the sorted_freqs

        # What is missing is that we need a way to link the nodes and the array. 
        # I think that the array should actually store the nodes as well.
        # We could create leaf nodes for everything in the array, then when we get rid of them we are just inserting a node with a new frequency that points to two existing nodes So we can safely delet ethem from the array. 
    # Depth first search to generate encoding table
        # Start at root
        # Add edge 

    # in our array as well, we much need a custom comparison: becaue we will need to store both the node and the frequency, we will need a tuple and set custom comparison as the first element of the tuple (freq)

def encoding_table(root: Node) -> list[int]:
    """Generate encoding table from graph.
    :input: the root node of the graph
    :output: array of size alphabet that stores the binary encoding of that letter"""
    # Implement some kind of depth first search

    # Start at root node
    # we re run encoding table for both edges, and pass in the encoding so far. Ie a string. 
    # Base case:
        # if we are at a leaf, then return the string passed in. 

def frequencies(ascii_start: int, ascii_end: int, txt: str) -> list[int]:
    """Generate an array of size alphabet, that stores the frequency of each character"""
    pass

def sorted_frequencies(freqs: list[int]) -> list[int]:
    pass


"""
Proofs:
    Why is huffman encoding optimal?
        Get all of the characters in increasing frequencies: ci
        Draw the length of the representation: li
        c1, c2, c3...
        l1, l2, l3...
        L = the encoding length/ measure/ observed encoding length is li*ci for all i
        For a encoding to be optimal, L is an absolute minimum.


        The smallest total space for this is multiplying c1*l1, c2*l2, ci*li
        If this was not minimal, then some c1*l2 + c2*l1 < c1*l1 + c2*l2

Notes:
    For decoding, graph is necessary. 
    For encoding, table is necessary.
"""
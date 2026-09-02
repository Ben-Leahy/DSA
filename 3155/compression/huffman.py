from __future__ import annotations

"""Reflectoin from class. Just follow the class and if there are other things ii want to investigate note them down and do them later."""

"""
TODO
    Find a better data type to store the bits
    Change all of the noted functions to work with this data type
    Test

    This is left for if we need to do it for an assignment. Otheriwse knowledge is there.
"""
# How to encode the tree vs the sorted array that we need to refer to?
# How to deal with binary numbers?
class Edge: 
    def __init__(self, val:int, to_node:Node):
        self.val = val
        self.to_node = to_node
    # 1 or 0

# Change edges to self.left, self.right
class Node:
    def __init__(self, title:str, freq:int,  is_leaf:bool = False, edges:list[Edge] = []) -> None:
        self.title = title
        self.freq = freq
        self.is_leaf = is_leaf
        self.edges = edges

    def __lt__(self, other):
        return self.freq < other.freq

    def __le__(self, other):
        return self.freq <= other.freq


def frequencies(txt: str) -> list[int]:
    freqs = [0]*128
    for char in txt:
        freqs[ord(char)] += 1
    return freqs

def unique_frequencies(freqs: list[int]) -> list[int]:
    unique_freqs = []
    for freq in freqs:
        if freq != 0:
            unique_freqs.append(freq)
    return unique_freqs

def create_sorted_nodes(unique_freqs: list[int]) -> list[Node]:
    nodes:list[Node] = []
    for i, freq in enumerate(unique_freqs):
        if freq != 0:
            nodes.append(Node(chr(i), freq))
    nodes.sort()
    return nodes


def huffman_graph(nodes: list[Node]) -> Node | None:
    """
    Construct graph from nodes containing char and freq.
    This is used for decoding.  

    :input: list[ Node(title, freq, is_leaf, edges)
    :output: root node of the graph"""
    # TODO this doesn't work for nodes of length less than 2
    root = None
    while len(nodes) >= 2:
        # Select top 2 nodes, and combine
        title = nodes[0].title + nodes[1].title
        freq = nodes[0].freq + nodes[1].freq
        is_leaf = False
        edges = [Edge(0, nodes[0]), Edge(1, nodes[1])]
        root = Node(title, freq, is_leaf, edges)

        # Replace old nodes with new
        nodes = nodes[2:]
        # TODO Change this to a bubble sort so that it had better time complexity. 
        nodes.append(root)
        nodes.sort()

    return root

def encoding_table(root: Node) -> list[list[int]]:
    """Generate encoding table from graph.
    :input: the root node of the graph
    :output: array of size alphabet that stores the binary encoding of that letter"""
    # Implement some kind of depth first search
    # We probably want to output an array of size alphabet. 
    # Then it is O(1) lookup.
    # TODO this function will also need ot be changed after 
    encoding_table = [[]] * 128
    dfs(root, [], encoding_table)
    return encoding_table


def dfs(node: Node, bits: list[int], encoding_table: list[list[int]]) -> None:
    # TODO We are starting with using an array of integers to represent the binary number, then we can convert
    # To a better suited bit focussed data type.
    if node.is_leaf:
        encoding_table[ord(node.title)] = bits
    else:
        bits0 = bits.copy()
        bits1 = bits.copy()
        bits0.append(node.edges[0].val)
        bits1.append(node.edges[1].val)
        dfs(node.edges[0].to_node, bits0, encoding_table)
        dfs(node.edges[1].to_node, bits1, encoding_table)
    return None

def encode(txt:str, encoding_table):
    # TODO this changes with data type as well
    encoding = []
    for char in txt:
        encoding += [encoding_table[ord(char)]]
    return encoding

def decode(encoding, root:Node):
    # TODO this changes with data type as well.
    output = ''
    curr_node = root
    for bit in encoding:
        if curr_node.is_leaf:
            output += curr_node.title
        else:
            curr_node = curr_node.edges[bit]

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

Huffman explanation:
    Construct a deterministic variable length encoding for characters. 
        This is necessary to compress - we can store more common examples with shorter characters. 
        This needs to be prefix free to go in both directions
        The basic idea is to store each encoding as a path to a leaf in a strict binary tree. This way no leaf is a prefix of another leaf.
        This generates the decoding graph.


Notes:
    For decoding, graph is necessary. 
    For encoding, table is necessary.
"""
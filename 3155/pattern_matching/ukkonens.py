class Node:
    def __init__(self):
        self.suffix_index = None
        self.is_leaf = None
        self.edges: list[Edge] = []


class Edge:
    def __init__(self):
        self.start = None
        self.end = None
        self.to_node: Node|None = None

def ukkonens(txt: list[str]):
    r = Node()
    current = r

    # Each iteration of this loop makes an implicit suffix tree from txt[1..i]
    for i in range(txt):
        j = 0 # what
        suffix_length = i - j + 1
        suffix_length_remaining = suffix_length
        # Traverse
        # from current node, we need to traverse i-j + 1. 
        traversing = True
        while traversing:
            next_edge = None
            for edge in current.edges:
                if txt[edge.start] == txt[j]:
                    next_edge = edge
                    edge_length = next_edge.end - next_edge.start + 1
                    # COntinue traversal
                    if edge_length < suffix_length_remaining:
                        suffix_length_remaining -= edge_length
                        pass #continue traversal 

                    # TODO we need to distinguish between rule 2r and 3 here: did we find teh string we are after?
                    if edge_length > suffix_length_remaining:
                        # Rule 3
                        if txt[next_edge.start : next_edge.end + 1] == txt[i + 1 - suffix_length_remaining  : i + 1]:
                            pass
                        else:
                            # Rule 2 regular: split an edge, create a node
                            # traverse until we get to a letter that mismatches, k. Then create a new node prev...k-1. then k..., and also whatever the other letter is ...
                            pass

                    # Rule 2 alternate:
                    if edge_length == suffix_length_remaining and next_edge.to_node.is_leaf == False:
                        traversing = False
                        pass
                    
                    # Rule 1
                    if next_edge.end - next_edge.start + 1 == suffix_length_remaining and next_edge.to_node.is_leaf == True:
                        traversing = False
                        pass

        pass


# Do we use suffix links functionally any differently to the rest?
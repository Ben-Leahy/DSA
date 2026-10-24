Maximum cardinality matching on unweighted bipartite graph. 
Optimal matching on weighted bipartite graph. 

Matching:
    When no node has a degree greater than 1. 
    Alternatively, no two edges share a vertex. 
    A matching has a number of edges. 

# Maximum cardinality matching
## Definition
    Maximum number of edges in a cardinality. 
    This is bounded by the minimum of edges in each set. 
    The number of edges in the maximum cardinality matching is M

## Solving approach 1
    Use max flow. Add in a source and sync. All edges have a max flow of 1, and are directed. (edges from source to node, and node to sync are also 1 which ensures that a node can't have more than 1 edge) solve. 
    Run Ford Faulkerson. Initialise all flows to 0. Residual flow is capacity - flow, which goes in the opposite direction. We find a path which augments. 

## Solving approach 2
    Augmenting based on alternating paths.
    Alternating paths:
        A path which alternates between matched and unmatched eges. (edges which belong in M and ones which don't)
        It has to be a simply path (no loops)
        It can start on matched or unmatched and be any length including 0. 
        
    Augmenting alternating path:
        The start and end edges are unmatched. 
        The number of unmatched edges += number of matched edges. 
        -> the number of edges is odd. 
        The shorted augmenting path has a length of 1

    Using augmenting alternating paths:
        Find one, then swap all edges. This has increased the number of matched edges by 1. 
        TODO?? how can we ensure that it doesn't break our constraints? 

        start with an empty matching (Or a greedy matching)
        Repeatedly search for an augmenting path:
        1. start with unmatched vertices from set X
        2. BFS/DFS follow all edges from this edge to nodes in Y. From a matched vertex in Y, follow an edge back to X. 
        From an unmatched vertex in Y, stop we have found one. 

    Augmentation theorem:
        A matching has maximum cardinality if and only if there is no augmenting path. 
        M, M*, M - M*. Every node has a degree 0, 1 or 2. 
        This means that we can divide into partitions, they are either just one node, a path, or a cycle. (If a node has a degree of two, then the node has one edge from each M and M*)
        M is the current, and M* is an ideal case. 
        If M is not maximal, then we will be able to find some path that exists in the set difference: odd length starting and ending with something not in M. 




Perfect matching:
    Every vertex is included in the maximum cardinality. 
    ie, |M| = |V| / 2


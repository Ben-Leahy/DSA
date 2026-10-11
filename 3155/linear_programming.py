"""
Uni lecture:
Non-basic: fixed
basic: non fixed

NAIVE
There are constraint functions
Then there is the overall function we are trying to maximise

Constraints create a convex polyhedron containing all possible valid values of decision variables.
Then the overall function can sweep towards it until the first intersection. 
We know this will be on the edge of the ocnvex polyhedron, and therefore at a corner, or vertex. 
This generlaises to n dimensions (even if it is paralell to a line or plane it will include a vertex)

So we can change inequalities to equalities by including slack or surplus variables. 
Then we can solve by setting any combination of m variables to 0
Then we calculate the objective function based on the calculated variables. 
Then restrict the answers if the calculated slack or surplus variables fail ( >=0 or <=0)
Then take the maximum



"""

"""
Questions
My solution isn't always worse, it's only worse if k^z > n. Ie 9^m in the worse case (all 0s) > n

The things that happened in work the other day

When we say minim increase (slides 28-29) is that because:
     minimum increase is the same as maximum increase which doesn't make a slack or surplus variable break its constraints?
"""
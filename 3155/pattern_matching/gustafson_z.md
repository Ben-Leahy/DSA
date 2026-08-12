## Complexity proof
The time complexity is bounded by the number of iterations + the number of character comparisons = number of iterations + number of mismatches + number of matches
    -> Because the only non O(1) operations which are completed in an iteration are character comparisons. 

Base cases:
    Base cases are clearly maximum of O(n)

Iterations:
    Inductive case has O(n) iterations. 

Now we just need to prove that the number of character comparisons is linear:
    Character comparisons are either matches or mismatches. 
    Mismatch:
        When a mismatch occurs, the sub-loop performing character comparisons immediately ends, followed by O(1) comparisons. 
        -> We only have 1 mismatch per iteration
        -> Iterations are bounded by n
        -> mismatches are bounded by n
    Matches:
        r only increases when we have a match, and whenever we have a match r increases.
        -> r is never decreased. 
        -> r therefore is monatomically increasing with each iteration
        -> r cannot increase beyond n-1, 
        -> r is bounded by n
        -> the number of matches is bounded by n

Our total complexity = number of iterations + number of mismatches + number of matches
= n + n + n
= O(n)

Our best case is also O(n), ie with a string of aaaaaaa...
Hence the application is also theta(n)

For Space:
Our z list is length n, then plus O(1) constants, clearly bounded by n. 
"""




## Notes

# the l box is a function of the r value: lk = rk - zk + 1
#  lengtyh -= end point - start point + 1


We are prepprocessing. string s.
The z value is an array, indexer is k. z[k] is the length of the maximum substring starting at s[k] which matches s. Or, z[k] is the maximum prefix of s matched by the substring starting at s[k].The length of the longest substring starting at k that matches the prefix. 
The substring from s[k] to s[k + z[k]] matches the prefix of s from s[0] to s[z[k]]

r is right most of z box. strictly non-decreasing
l is left most. If multiple have the same r value, we can pick either l value. 

What are these formulas??? I was writing notes oops. Let's come back to them. The point of them is to show that we don't need to store or calculate something? The point is you only need 2 of start point and z value and end point (r value). Is start value l? Um not quite remember the formulas. Start value is k.

r is updated to (start + z - 1)

start point, z value (inputs) -> r value or endpoint is start point + z value - 1


NB when the initial case doesn't have a match, then with 1 based indexing, we can define l and r as 0. But when programming with 0 based indexing we need some other character... null or negative. (what would happen if we just set it to 0 though?)

k is always >= l


case 1:


case 2:
because we know that k is some amount greater than l, then we know that the k value was already calculated at z[k-l]
So then we only need to compare from s[r+1], if we find a mismatch we are done, or we can continue and update the box. 

case 2b:
equal to
three betas. right most is x, middle is y: y!=x. Left most is v:v!=y, but v could equal x, so we have to check and the new z value is at least what the mirrored z value is. 

greater than
take that z value from the mirrored, then go from z[k + z[mirrored]] and compare going forward? 

TODO when I code this I am going to need to make sure my indexing is correct for 0 based indexing. 
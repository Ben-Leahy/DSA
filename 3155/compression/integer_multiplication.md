When actually implementing this, we implement in base 2^32, because we have hardware that can multiply this in O(1)
Ie, divide and conquer until we get to 2d = 2^32

1. write the break down of 
TODO:
    explicityl decompose
    T(2d) = 3*T(d) + cd

    Then try the proof again using base beta

# Regular exponentiation
a^b = a^b/2 * a^b/2

# Modular exponentiation

reinman hypothesis, if 100% of the numbers lie on this line then we have a close form solution for prime numbers. 
... but even if only 70% of these lie on that line, does that mean 70% of random prime numbers generated aren't secure. 

euclids proof that there are infinite primes
if you assume there are finite number of primes. Every number can be divisible into it's prime factors, 
then you can show by construction that you can create a new prime number from the existing ones?

what are siving algorithms

improvements on naive:
1. stop at root (n) (proof? n = p*q, let p>=q, then p*q <= p^2... one factor has to be smaller than n. if both factors were greater than root n then p*q would be greater than n)
2. don't test for multiples of numbers we have tested. 

Congruence class definition, 
a==b mod n, if (a - b) = k * n

-11 = -2*7 + 3
How many times does 7 go into -11? it does in -2 times, with a remainder of 3. 

561/3
600/3 = (561 + 39)/3
sum of digits theorm

we don't want to pick a = n-1 because the expansion of (n-1) ^ (n-1) is always divisible by n

if n is 2, prime, if n is not too and hte last digit is 0 then it's composite. 

import math
ns = [i for i in range(1, 19)]
# exclude resising at n = 1
resizes = [0, 1, 2, 2, 3, 3, 3, 3, 4]
b = [0] + [math.floor(math.log2(n) + 1) for n in ns]
# include
resizes = [1, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6]
b = [1] + [math.floor(math.log2(n) + 2) for n in ns]
# a = [math.floor(math.log2(n + 1) + 1) for n in ns]

# bb = [math.floor(math.log2(n)) for n in ns]
print("ns      : ", ns)
print("resizes : ", resizes)
print("b       : ", b)
# print("bb      : ", bb)
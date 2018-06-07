import numpy as np

c1 = np.array([1, 2])
c2 = np.array([3, 4])

c1 = c1+c2
c1 -= 2
c2 = c2**2
c2 *= 1
c3 = c1 * c2
val = c1.dot(c2)
print(c1, c2, c3)
print(c1 > 2)


aa = np.random.random(4)
print(aa)
la = np.arange(4)
print(la)
aa += la
print(la)           # error as aa is float and la is int type


lm = np.array([1, 2, 3])
print("SUM:", lm.sum(), "MIN:", lm.min(), "MAX:", lm.max())

b11 = np.arange(12).reshape(3, 4)
print("ARRAY b11:\n", b11)
print("SUM of each row:\n", b11.sum(axis=0))
# axis = 0   each column
# axis = 1   each row        for two dimensional array

print("MIN of b11:\n", b11.min(axis=1))      # min of each row
print("Cumulative sum along each row \n", b11.cumsum(axis=1))

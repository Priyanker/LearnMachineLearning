import numpy as np

# Evenly spaced:
a = np.arange(10)
print(a)            # [0 1 2 3 4 5 6 7 8 9]
print("Type of a:", a.dtype.name)

a1 = np.array([1, 2, 3])
print(type(a1))
# print(a1.data)        #<memory at 0x000001A8AB6D6DC8>
# start, end (exclusive), step
b = np.arange(1, 9, 2)
print(b)            # [1 3 5 7]


# by number of points:
c = np.linspace(0, 1, 5)          # start, end, num-points
print(c)

d = np.linspace(0, 1, 5, endpoint=False)
print(d)


# Common arrays:
e = np.ones((3, 3))
print(e)
# [[1. 1. 1.]
# [1. 1. 1.]
# [1. 1. 1.]]

f = np.zeros((2, 2))
print(f)
# [[0. 0.]
# [0. 0.]]

g = np.eye(3)   # Identity matrix
print(g)
# [[1. 0. 0.]
# [0. 1. 0.]
# [0. 0. 1.]]

h = np.diag(np.array([1, 2, 3, 4]))
print(h)
# [[1 0 0 0]
# [0 2 0 0]
# [0 0 3 0]
# [0 0 0 4]]

h1 = np.empty((3, 2))
print("Array h1:\n", h1)

# print(h.size)             # no. of elements


# np.random: random numbers
i = np.random.rand(5)       # uniform in [0, 1]
print("Array i:\n", i)

j = np.random.randn(5, 2)      # Gaussian
print("Array j:\n", j)

k = np.random.seed(1)
print(k)

m = np.array([[1, 3], [2, 4]], dtype=complex)   # dtype= float
print(m)


n = np.arange(12).reshape(4, 3)
print(n)


# If an array is too large to be printed, NumPy automatically skips the central
# part of the array and only prints the corners:
print(np.arange(10000))
print(np.arange(10000).reshape(100, 100))

print(np.sin(np.degrees(180)))

import numpy as np

a = np.arange(10)**3
print(a[2])
print(a[2:5])

a[:6:2] = -1000
print(a)
print(a[::-1])
for i in a:
    print(i**(1/3))


def f(x, y):
    return 10*x+y


b = np.fromfunction(f, (5, 4), dtype=int)
b
# array([[0,  1,  2,  3],
#       [10, 11, 12, 13],
#       [20, 21, 22, 23],
#       [30, 31, 32, 33],
#       [40, 41, 42, 43]])
print(b[2, 3])
# 23
print(b[0:5, 1])                       # each row in the second column of b
# array([ 1, 11, 21, 31, 41])
print(b[:, 1])                        # equivalent to the previous example
# array([ 1, 11, 21, 31, 41])
print(b[1:3, :])                      # each column in the second and third row of b
# array([[10, 11, 12, 13],
#        [20, 21, 22, 23]])
print("ASS", b[1,...])

print(int(np.floor(3.4)))

b1 = np.floor(10*np.random.random((3, 4)))

import numpy as np
a = np.arange(3)
b = np.full(3,5)
print(a, b, sep="\n")
print("a+b:\n", a + b)
print("a+5:\n", a+5)

print()

M = np.ones((3, 3))
print("M:\n", M)
print("M+a:\n", M + a)

print()

x = np.arange(3)
y = np.arange(3)[:, np.newaxis]

print('x:\n', x)
print('y:\n', y)
print("x+y:\n", x + y)
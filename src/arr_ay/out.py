import numpy as np

x = np.arange(5)
y = np.empty(5)

print("x:\n", x)
print("y:\n", y)

np.multiply(x, 10, out=y)
print("y:\n", y)

print()

new_y = np.zeros(10)
np.power(2, x, out=new_y[::2])
print("new array:\n", new_y)
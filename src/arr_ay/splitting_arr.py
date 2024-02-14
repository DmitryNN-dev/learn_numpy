import numpy as np

x = [1, 2, 3, 7, 99, 99, 7, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])  # 99, 99 - [3, 5]
print(x1, x2, x3, sep="\n")
print("Done")

# np.vsplit, np.hsplit
grid = np.arange(16).reshape((4, 4))
print(grid)
print()

upper, lower = np.vsplit(grid, [2])
print("upper: \n", upper)
print("lower: \n", lower)
print()

left, right = np.hsplit(grid, [2])
print("left: \n", left)
print("right: \n", right)
print()

# np.dsplit
ar1_3d = np.arange(8).reshape((2, 2, 2))
print("ar1_3d: \n", ar1_3d)
print()

first, second = np.dsplit(ar1_3d, 2)
print("first: \n", first)
print("second: \n", second)
import numpy as np

arr = np.arange(1, 10, dtype=float)
print("arr", arr, "\n")

print("reshape:")
grid = arr.reshape((3, 3))
print(grid, "\n")

# вектор строка:
x = np.array([1, 2, 3])
x.reshape((1, 3))
print(x)

# вектор строка посредством newaxis:
x1 = x.copy()
x1[np.newaxis, :]
print(x1, "\n")

print(x.reshape((3, 1)))
print(x[:, np.newaxis])
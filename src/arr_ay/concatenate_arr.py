import numpy as np

x = np.arange(1, 4)  # look alike to np.array([1, 2, 3])
y = np.array([3, 2, 1])

print(np.concatenate([x, y]))

# more than 2 arrays
z = [10, 10, 10]

print(np.concatenate([x, y, z]))

# concatenate by first axis of coordinate
grid = np.array([[1, 2, 3],
                 [4, 5, 6]])

print(np.concatenate([grid, grid[::-1]]))

# concatenate by second axis (with zero index)
print(np.concatenate([grid, grid[::-1]], axis=1))
print()

# vertical integration:
x = np.array([1, 2, 3])
grid = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("np.vstack: \n", np.vstack([x, grid]))

# horizontal integration
y = np.array([[7],
              [8]])
print("np.hstack: \n", np.hstack([grid, y]))

# by fierd axis:
print("np.dstack: \n", np.dstack([grid, grid]))


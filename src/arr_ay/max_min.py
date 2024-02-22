import numpy as np

a_rray = np.random.randint(1, 10, size=(1, 10))
print(a_rray)
print("min:\n", np.min(a_rray))
print("max:\n", np.max(a_rray))

print()

M = np.random.random((3, 4))
print(M)
print("M.sum()\n", M.sum())
print("min для каждого столбика:\n", M.min(axis=0))
print("min для каждой строки:\n", M.min(axis=1))

# --//-- с min используется .max
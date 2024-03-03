import numpy as np

np.random.seed(132121)
ar1 = np.random.randint(1, 7, (7, 3))
print('ar1:\n', ar1)

ar2 = np.random.randint(1, 7, (7, 3))
print('ar2:\n', ar2)

print("ar1*ar2:\n", np.multiply(ar1, ar2))

# Нахождение определителя для ar1
det_ar1 = np.linalg.det(np.dot(ar1.T, ar1))
print("Определитель для ar1:\n", det_ar1)

# Нахождение определителя для ar2
det_ar2 = np.linalg.det(np.dot(ar2.T, ar2))
print("Определитель для ar2:\n", det_ar2)

# Решение систем уравнений:

# 2x + 3y = 8
# 4x - y = -2

# A = [[2, 3],
#      [4, -1]]
# x = [[x],
#      [y]]
# B = [[8],
#      [-2]]

A = np.array([[2, 3], [4, -1]])
B = np.array([8, -2])
X = np.linalg.solve(A, B)
print("x=", X[0])  # =1
print("y=", X[1])  # =2
# проверка
print(2*X[0] + 3*X[1])
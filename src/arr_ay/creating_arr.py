import numpy as np

lst = [1, 4, 2, 5, 3]
arr = np.array(lst)  # [1, 4, 2, 5, 3]
print(arr, "\n")

# [0 0 0 0 0 0 0 0 0 0] 
arr = np.zeros(10, dtype=int)
print(arr, "\n")

arr = np.ones((3, 7), dtype=int)  # [[1 1 1 1 1 1]
print(arr, "\n")                  #  [1 1 1 1 1 1]
                                  #  [1 1 1 1 1 1]]

arr = np.full((2, 3), 3.14)  # [[3.14 3.14 3.14]
print(arr, "\n")             #  [3.14 3.14 3.14]]

arr = np.arange(0, 10, 2)  # [0 2 4 6 8]
print(arr, "\n")

arr = np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1.  ]
print(arr, "\n")

arr = np.random.random((3, 4))  # array with random value from 1 to 2
print("Array:", arr, "\n")

arr = np.random.normal(0, 1, (3, 3))
print(arr, "\n")

arr = np.random.randint(0, 10, (3, 2))  # the gap: [0, 10)
print(arr, "\n")

arr = np.eye(3)  # the unit matrix (3x3)
print(arr, "\n")

arr = np.empty(6)
print(arr, "\n")

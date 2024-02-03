import numpy as np

np.random.seed(0)  # start value for np.random.randint()

x1 = np.random.randint(10, size = 6)  # one-dimensional array
x2 = np.random.randint(10, size = (3, 4))  # two-dimensional array
x3 = np.random.randint(10, size = (3, 4, 5))  # three-dimensional array

# ndim - размерность, shape - форма(размерность каждого измерения), size - общий размер:
print("x3.ndim:", x3.ndim)
print("x3.shape:", x3.shape)
print("x3.size:", x3.size)

# dtype - тип данных
print("dtype:", x3.dtype, "\n")

# itemsize - размер (в байтах) у каждого элемента
print("itemsize:", x3.itemsize, "bytes")

# nbytes - полный размер массива в байтах
print("nbytes:", x3.nbytes, "bytes", "\n")
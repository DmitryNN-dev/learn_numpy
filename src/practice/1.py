import numpy as np

np.random.seed(132121)
ar = np.random.randint(1, 999, (101, 2))
print('ar:\n', ar)

mean_of_ar = np.mean(ar)
print("ar.mean():\n", mean_of_ar)
median = np.median(ar)
print("median:\n", median)

print()

# Стандартное отклонение
std_dev_axis0 = np.std(ar, axis=0)
std_dev_axis1 = np.std(ar, axis=1)
std_dev = np.std(ar)
print("std_dev_axis0:\n", std_dev_axis0)
print("std_dev_axis1:\n", std_dev_axis1)
print("std_dev:\n", std_dev)

print()

min_of_ar = np.min(ar)
print("min:\n", min_of_ar)
max_of_ar = np.max(ar)
print("max:\n", max_of_ar)

print()

# Индекс искомого элемента массива:
indices = np.where(ar == 992)
print("indices:", indices)
# проверем:
if ar[(65, 1)] == 992:
    print("992?:\n", True)
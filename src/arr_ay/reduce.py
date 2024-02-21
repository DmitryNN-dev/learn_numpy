import numpy as np

# Многократное повторение операции:
x = np.arange(1, 11)

summ = np.add.reduce(x)
print("summ:\n", summ)

mult = np.multiply.reduce(x)
print("mult:\n", mult)

# Сохроняя все результаты вычислений:
save_s = np.add.accumulate(x)
print("save_s:\n", save_s)

save_m = np.multiply.accumulate(x)
print("save_m:\n", save_m)

print()

# Известные аналоги:
s = np.sum(x)
print("s:\n", s)
prod = np.prod(x)
print("prod:\n", prod)
cumsum = np.cumsum(x)
print("cusum:\n", cumsum)
cumprod = np.cumprod(x)
print("cumprod:\n", cumprod)
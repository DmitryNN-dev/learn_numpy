import numpy as np
x = np.arange(1, 6)

# Массив повторяется в столбик, место пересечения дают остальные значения при переумножении:
print(np.multiply.outer(x, x))

print()

# --//--, но add
print(np.add.outer(x, x))

print()
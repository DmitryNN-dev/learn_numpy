from scipy import special as s
import numpy as np

# Гамма функции (обобщенные факториалы) и тому подобное
x = np.arange(1, 12, 5)
print("x:\n", x)
print("gamma(x):\n", s.gamma(x))
print("ln|gamma(x):\n", s.gammaln(x))
print("beta(x, 2):\n", s.beta(x, 2))

print()

# функция ошибок (интеграл от Гфуссовой функции), дополнительная и обратная к ней функции
x = np.array([0, 0.3, 0.7, 1.0])
print("erf(x:\n)", s.erf(x))
print("erfc(x):\n", s.erfc(x))
print("erfinv(x):\n", s.erfinv(x))

# and more another func
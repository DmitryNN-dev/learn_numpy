import numpy as np

np.random.seed(0)
arr = np.random.randint(1, 10, size=(2, 3))
print(arr)

print("arr+arr:\n", np.add(arr, arr))
print("arr-arr:\n", np.subtract(arr, arr))
print("negative:\n", np.negative(arr))
print("arr*arr:\n", np.multiply(arr, arr))
print("arr/arr:\n", np.divide(arr, 4))
print("arr//arr:\n", np.floor_divide(arr, 3))
print("arr**3:\n", np.power(arr, 3))
print("remains of arr/3:\n", np.mod(arr, 3))

print()

new_arr = np.arange(-9, 1)
print(new_arr)
print("abs(new_arr):\n", np.abs(new_arr))
print("abs(new_arr):\n", np.absolute(new_arr))

print()

just_arr = np.array([3-4j, 4-3j, 2+0j, 0+1j])
print(just_arr)
print(abs(just_arr))

print()

theta = np.linspace(0, np.pi, 3)
print("theta:\n", theta)
print("sin(theta):\n", np.sin(theta))
print("cos(theta):\n", np.cos(theta))
print("tg(theta):\n", np.tan(theta))

print()

x = [-1, 0, 1]
print("x:\n", x)
print("arcsin(x):\n", np.arcsin(x))
print("arccos(x):\n", np.arccos(x))
print("arctg(x):\n", np.arctan(x))

print()

x = [1, 2, 3]
print("x:\n", x)
print("e^x:\n", np.exp(x))
print("2^x:\n", np.exp2(x))
print("3^x:\n", np.power(3, x))

print()

x = np.arange(1, 11, 2)
print("x:\n", x)
print("ln(x):\n", np.log(x))
print("log2(x):\n", np.log2(x))
print("log10(x):\n", np.log10(x))

print()

x = [0, 0.001, 0.01, 0.1]
print("x:\n", x)
print("exp(x)-1:\n", np.expm1(x))
print("log(1+x):\n", np.log1p(x))
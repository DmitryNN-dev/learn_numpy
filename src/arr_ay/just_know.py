import numpy as np

np.random.seed(0)

# problem - it's slow
def compute_reciprocals(value):
    output = np.empty(len(value))
    for i in range(len(value)):
        output[i] = 1.0 / value[i]
    return output

values = np.random.randint(1, 10, size=5)
print(compute_reciprocals(values))

# it's better:
print(1.0/values)
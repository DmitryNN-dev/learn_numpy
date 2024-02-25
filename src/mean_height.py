import numpy as np

heights = np.linspace(160, 200, 42)
print(heights)

print("Mean height:", heights.mean())
print("Standart deviation:", heights.std())
print("Min height:", heights.min())
print("Max height:", heights.max())

print()

print("25:\n", np.percentile(heights, 25))
print("Median:", np.median(heights))
print("40th:\n", np.percentile(heights, 40))
import numpy as np
import cv2

img = cv2.imread('example.jpg')
img = img/1.0

if img is not None:
    ar = np.array(img)

print(ar)
print("ar.ndim():\n", ar.ndim)
print("ar.shape():\n", ar.shape)

# for i in img:
#     i *= 0.2
# cv2.imshow("new_img:\n", img)
# cv2.waitKey(0)

compare_mask = ar < 80
print("compare_mask", compare_mask)

opposite_compare_mask = ~(ar >= 80)
print("opposite_compare_mask", opposite_compare_mask)

print(ar[opposite_compare_mask])
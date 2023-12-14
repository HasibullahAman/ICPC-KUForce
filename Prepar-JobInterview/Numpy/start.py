import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ndmin=5)
# print(arr)
# print(arr.ndim)
# print(arr)

arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 0], [10, 11]], [[13, 14], [15, 16]]], ndmin=5)
print(arr2)
print(arr2.ndim)

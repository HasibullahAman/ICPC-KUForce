import numpy as np

myArr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# print(myArr[1::2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# print(arr[0:2, 1:4])
# print(arr[2,3])


arr = np.array([1, 2, 3, 4])
arrNew = arr.astype(dtype='i8')
print(arrNew.dtype)

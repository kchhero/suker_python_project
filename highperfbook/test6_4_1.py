import numpy as np

array1 = np.random.random((10, 10))
array2 = np.random.random((10, 10))

print("array1 id = " + str(id(array1)))
print("array2 id = " + str(id(array2)))

array1 += array2

print("array1 id = " + str(id(array1)))

array1 = array1 + array2

print("array1 id = " + str(id(array1)))

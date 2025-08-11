#Exercise 1 : Create two dimensional 3*3 array and perform ndim, shape, slicing operation on it.
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("ndim:", arr.ndim)
print("shape:", arr.shape)
print("First row:", arr[0])           
print("First column:", arr[:, 0])     
print("Element at [1,2]:", arr[1, 2]) 
print("first 2 rows, cols 1-2:\n", arr[:2, 1:3])

#Exercise 2: Create one dimensional array and perform ndim, shape, reshape operation on it
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print("ndim:", arr.ndim)
print("shape:", arr.shape)
reshaped_arr = arr.reshape(2, 3)
print("Reshaped array:\n", reshaped_arr)
print("New shape:", reshaped_arr.shape)
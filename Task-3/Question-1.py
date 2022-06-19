import numpy as np
arr = np.array([10, 11, 12, 13, 14])
print("The array : ")
print(arr)
p = 5
new_arr = np.zeros(len(arr) + (len(arr)-1)*(p))
new_arr[::p+1] = arr
print("\nNew array : ")
print(new_arr)
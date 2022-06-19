import numpy as np
first_array = np.random.randint(0, 2, 6)
print("First array : ")
print(first_array)
second_array = np.random.randint(0, 2, 6)
print("Second array : ")
print(second_array)
array_equal = np.allclose(first_array, second_array)
print(array_equal)
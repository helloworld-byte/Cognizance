import numpy as np
X = 4
Y = [[6,2],[9,1]]
# np.dot(arr1, arr2) returns the scaler or dot product.
print("-----Dot Product-----")
print("A = ",X)
print("B = ",Y)
print("Output = ",np.dot(X,Y))

X = [[2,5],[2,2]]
Y = [[6,2],[9,1]]
# np.dot(arr1, arr2) returns the scaler or dot product.
print("-----Matrix Product-----")
print("A = ",X)
print("B = ",Y)
print("Output = ",np.matmul(X,Y))

#python code to demonstrate matrix addition,subtraction and multiplication

import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[4,5],[6,7]])
print("elements of first array :",)
print(A)
print("elements of second array :",)
print(B)
print("addition :")
print(np.add(A,B))
print("subtraction :")
print(np.subtract(A,B))
print("multiplication :")
print(np.dot(A,B))

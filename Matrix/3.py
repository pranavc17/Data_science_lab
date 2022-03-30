#find the sum of values in a matrix

import numpy as np

matrix = np.array([[2,4,6],[7,3,1],[4,8,2]])
col,row=matrix.shape
sum=0
for i in range(row):
    for j in range(col):
        sum +=matrix[i][j]

print("sum of values in the matrix ",sum)

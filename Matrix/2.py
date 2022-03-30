#find the number of row and column of a given matrix using numpy

import numpy as np

matrix= np.array([[2,4,6],[7,3,1],[4,8,2],[7,1,5]])
row,column=matrix.shape
print("number of rows :",row)
print("number of column :",column)

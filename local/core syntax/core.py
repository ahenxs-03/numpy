#1. create numpy arrays
import numpy as np
# 1 dimension array/vector
vector=np.array([1,2,3])
# 2 d array/ matrix
matrix=np.array([[1,2,3],[4,5,6]])
# 3 d array /tensor
tensor=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
#more dimension possible as well
#method 2=> by fixing data type
# array with string
data=np.array([['price','distance'],['10','2km'],['12','500m']])# can be any data type but homo
print(data)
#data=np.array([['price','distance'],['10','2km'],['12','500m']],dtype=int)# dtype convert all entries into dtype
# error
data2=np.array([['price','distance'],['10','2km'],['12','500m']],dtype=bool)
print(data2)# tru truie true true....
# method 3. arange: works as same as range works in python

#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#


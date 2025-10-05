import numpy as np
from numpy._core.fromnumeric import ndim
from numpy._core.numeric import array

array_1 = np.array([1, 2, 3, 4])
#print(array_1)
#print(array_1.ndim)
#print(array_1.shape)
array_2 = np.array([[1,2], [3,4]])
#print(array_2)
#print(array_2.ndim)
#print(array_2.shape)
array_zeros = np.zeros((2,3))
#print(array_zeros)
array_ones = np.ones(4, dtype=np.int64)
#print(array_ones)
#print(array_ones.dtype)
x1 = np.full(10, 5.4)
#print(x1)
aranged_array = np.arange(0.0, 11, 1)
#print(aranged_array)
lin_array = np.linspace(0, 10, 11)
#print(lin_array)
log_array = np.logspace(0,2,5)
#print(log_array)
x = np.array([-1,0,1])
y = np.array([-2,0,2])
X,Y = np.meshgrid(x,y)
#print(X)
#print(Y)
def f(x):
    y = np.ones_like(x)
    y = y*x 
    return y

print(f([1,4,5]))


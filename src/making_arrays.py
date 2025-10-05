import numpy as np

# data = np.array([[1, 2], [3, 4], [5, 6]])
# print(type(data))
# print(data)
# print(data.ndim)
# print(data.shape)
# print(data.size)
# print(data.dtype)
# print(data.nbytes)


# data_2 = np.array([1, 2, 3], dtype=int)
# print(data_2)

# data_3 = np.array([1, 2, 3], dtype=float)
# print(data_3)

# data_4 = np.array([1, 2, 3], dtype=complex)
# print(data_4)
# print(data_4.dtype)

# data_5 = np.array([1, 2, 3], dtype=float)
# print(data_5)
# print(data_5.dtype)
# data_5 = np.array(data_5, dtype= int) # changing the type of an array
# print(data_5.dtype)
# print(data_5)

# data_5.astype(float) # another way of changing it

d1 = np.array([1, 2, 3], dtype=float)
d2 = np.array([1, 2, 3], dtype=complex)
d3 = d1 + d2

print (d3)
print ((d3).dtype) # dtype is converted to complex to allow for operation

print (d3.real) # real attribute of d3
print (d3.imag) # imaginary attribute of d3

print("Hello, I am using neovim!")

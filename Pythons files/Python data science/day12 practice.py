import numpy as np
#NumPy Module
# #Q2
# #1.
# print("The version is:",np.__version__)
# np.show_config()
# #2.
# Z = np.zeros(10)
# print(Z)
# #3.
# Z = np.zeros((10,10))
# print("%d bytes" % (Z.size * Z.itemsize))
# #4.
# nz = np.nonzero([1,2,0,0,4,0])
# print(nz)
# #5.
# Z = np.eye(3)
# print(Z)
# #6.
# Z = np.random.random(30)
# m = Z.mean()
# print(Z)
# print(m)

# #7.
# Z = np.ones((10,10))
# Z[1:-1,1:-1] = 0
# print(Z)

# #8.
# Z = np.zeros(10)
# Z[4] = 1
# print(Z)

# #9.
# x=np.ones((3,3), dtype=bool)
# print(x)

# #Q3.
# #1.
# my_array = np.array([1, 2, 3, 4])
# my_slice = my_array[1:3]
# print(my_slice)

# #2.
# my_vector = np.array([1, 2, 3, 4, 5, 6])
# selection = my_vector % 2 == 0
#
# print(my_vector[selection])

# #3.
# my_array = np.array( [1, 2, 3] )
# my_slice = my_array[1:3]
# my_slice = my_slice * 2
# print(my_slice)

# #4.
# my_array = np.array( [[1, 2, 3], [4, 5, 6]])
# my_slice = my_array[:, 1:3]
# print(my_slice)

# #5.

# first_matrix = np.array( [ [1, 2, 3], [4, 5, 6] ] )
# second_matrix = np.array([1, 2, 3])
# my_matrix=first_matrix + second_matrix
# print(my_matrix)

# #6.


# X = np.array( [ [ [ 1, 2,3], [ 4, 5, 6]],
# [ [7,8,9], [10,11,12] ] ] )
# print(X.shape)
# print(X.ndim)
# print(X.size)

# #Q4.
# sales = np.loadtxt('E:\Certificates courses\Data science with python\data.csv', delimiter=',', dtype='str')
# # print(sales)
# Name = sales[1: , 0]
# Mon=sales[ 0 , 1:]
# data=sales[1: , 1:]
# print(Name)
# print(Mon)
# print(data)

# #Q5.
# N = np.array([1,2,3,4,5])
# Fx = lambda x: 3*x*x + 5*x + 10
#
# print(Fx)


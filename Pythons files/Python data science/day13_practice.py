import numpy as np
# #Q2.

# x = np.array([1, 2, 3, 4])
# print("Original array:")
# print(x)
# print("Test if none of the elements of the said array is zero:")
# print(np.all(x))
# x = np.array([0, 1, 2, 3])
# print("Original array:")
# print(x)
# print("Test if none of the elements of the said array is zero:")
# print(np.all(x))

# #Q3.


# a = np.array([1, 0, -1, -4])
# print("Original array")
# print(a)
# print("Test element-wise for positive or negative infinity:")
# print(a>=0)

# #Q4.
# array=np.zeros(10)
# print("An array of 10 zeros: ")
# print( array)
# array=np.ones(10)
# print("An array of 10 onces: ")
# print(array)
# array=np.ones(10)*5
# print("An array of 10 fives:")
# print(array)

# #Q5.
# x = np.ones((10, 10))
# x[1:-1, 1:-1] = 0
# print(x)

# #Q6.

# array=np.random.randint(100 , size=(3,3))
#
# print("An array of 3 X 3 zeros:")
# print(array)
# print("An array of divisible by 3 and 5:")
# filter= (array%3==0) & (array%5==0 )
# print( array[ filter])

# # Q.7 Write a NumPy program to replace even number by 0 in 2D array.
#
# array=np.random.randint(100 , size=(3,3))
# print("An array of 3 X 3 zeros:")
# print(array)
# print("An array of divisible by 3 and 5:")
# filter= (array%2==0)
# array[ filter]=0
# print(array)
#
# # Q.8 What is the Output ?
# x = np.random.randint(100, size=5)
# print(x)
# x1 = np.random.rand(5)
# print(x1)
# x2= np.random.choice([3, 5, 7, 9], size=5)
# print(x2)
#
# # # Q.9
# is_prime = np.ones((100,), dtype=bool)
#
# # Cross out 0 and 1 which are not primes:
# is_prime[:2] = 0
#
# # cross out its higher multiples (sieve of Eratosthenes):
# nmax = int(np.sqrt(len(is_prime)))
# for i in range(2, nmax):
#     is_prime[2*i::i] = False
#
# print(np.nonzero(is_prime))

# #10. Write a NumPy program to create an array with values ranging from 12 to 38.

# n=np.arange(12,39)
# print((n))

# #Q11.
# n = np.arange(2, 11)
# m = n.reshape((3, 3))
# print(n)
# print(m)

# #Q12.
# A = np.array([3, 4, 6, 10, 24, 89, 45, 43, 46, 99, 100])
#
# f3 = (A % 3 == 0) & (A % 5 == 0)
# print(A[f3])
#
# f2 = A %5 == 0
# print(A[f2])
#
# f1 = A % 3 != 0
# print(A[f1])
#
# f4 = A % 3 == 0
# A[f4] = 42
# print(A)

# #Q13.
# A = np.zeros((3,4))
# B = np.zeros((3,4))
#
# print('Enter the Values of A [3 x 4] : ')
# for id, v in np.ndenumerate(A) :
#     A[id] = int(input('Enter Value : '))
#
# print('Enter the Values of B [3 x 4] : ')
# for id, v in np.ndenumerate(B) :
#     B[id] = int(input('Enter Value : '))
#
# C =A+B
#
# print(A)
# print(B)
# print(C)

# #Q14.
# SALE1= np.loadtxt('E:\Certificates courses\Data science with python\d13salesdata-1-6.csv', delimiter=',', dtype='str')
# SALE2= np.loadtxt('E:\Certificates courses\Data science with python\d13salesdata-7-12.csv', delimiter=',', dtype='str')
# SALE = np.hstack([SALE1,SALE2])
# SALE = np.delete(SALE, 7, 1)
#
# month= SALE[0 , 1:]
# names = SALE[1: , 0]
# data= SALE[1: , 1:].astype(int)
# print('Months are: ', month)
# print('Names are: ', names)
# print('data are:', data)
# print(data.sum(axis=1))
# print(data.sum(axis=0))
# r=data.sum(axis=1)
# s=data.sum(axis=1)
# r=dict(zip(names, s))
# print(r)
# print(data.max())
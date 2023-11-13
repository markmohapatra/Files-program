#Q2
#a to print in list
# a=range(1,21,2)
# print(list(a))

#or vertical 
# a=range(1,21,2)
# for i in a:
#     print(i)

#b
# b=range(4,41,4)
# for i in b:
#     print(i)

#to print in list 
# b=range(4,41,4)
# print(list(b))

#c
# c=range(1,11,1)

# for i in c:
#     p=i**2
#     print(p)
#to print in list 

# c=range(1,11,1)
# for v in c:
#   print(v*v, end=' ')
# print( )  
#d

# d=range(1,11,1)
# for v in d:
#   print(v*2.5, end=' ')
# print( )  

#e

# e=range(1,11,1)
# for v in e:
#   print(v*-5, end=' ')
# print( )  

#f
# f=range(1,11,1)
# for v in f:
#   print(v*-5, end=' ')
# print( )  

#Q3
# m=1
# n=10

# x=range(m,n+1)

# SO=SE=0
# if m<n:
#  for v in x:
#     if v%2==0:
#         SE=SE+v
#     else:
#         SO=SO+v
#  print('Sum of Even:', SE)
#  print('Sum of Odd:', SO)
# else:
#   print(m,n,'Range is not valid')

#Q4
# n=int(input("Enter End Value:"))

# for v in range(1,11):
#    print(v*n)

# #Q5
# n=int(input("Enter End Value:"))
# s=0
# for v in range(1,n+1):
#    s=s+v
# print("Sum:",s)


#Q6

# Month= ['Jan','Feb','Mar', 'Apr', 'May','Jun']

# for v,u in enumerate(Month):
#     print(v,u)
# #for v in enumerate(Month):
#     #print(v[0],v[1])
#to show odd number value
# for v,u in enumerate(Month):
#     if v%2==1:
#       print(v,u)

#Q7
# a=range(1,20,2)
# s=0
# for x,y in enumerate(a):
#     if x%2==0:
#         print(x,y)
#         s=s+y
# print('sum: ', s)

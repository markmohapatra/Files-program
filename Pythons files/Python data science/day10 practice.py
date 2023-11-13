# def Show(a,b):
#     # print(a)
#     t=a
#     a=b
#     b=t
#     # print(a)
#     # print(b)
# a=19
# b=20
# Show(a,b)
# print(a)
# print(b)

# #Q2 Write a lambda function to find the sum of 4 numbers.
# sumN= lambda s1,s2,s3,s4: s1+s2+s3+s4
# r=sumN(10,20,30,40)
# print("SUM", r)

# #Q3 Write a lambda function to calculate the area of circle.
# import math
# AreaC = lambda r : math.pi * r*r
# r=round(AreaC(10), 3)
# print(f"Area of Circle with radius: {10} = {r}")

# #Q4 Write a lambda function to calculate the factorial of a number.
# FACT=lambda n: 1 if n==0 else n* FACT(n-1)
#
# for n in range(1,6) :
#    r=FACT(n)
#    print(f"Factorial of {n} = {r}")

# #Q5 Write a function to calculate the sum of first 10 natural number.
# nSUM=lambda n : 1 if n==1 else n+nSUM(n-1)
#
# n=10
# r=nSUM(n)
# print(f"Sum of {n} Natural number = {r}")


##Q6  Write a lambda function to find the maximum from items of List collection passed as argument.
# MAXL=lambda L: max(L)
# x=[10,11,7,8,9]
# r=MAXL(x); print('Max : ', r)

##Q7  Write a function to find the maximum from the numbers passed as argument to the function. [ use Arbitrary Argument ]
# def MAXN(*N):
#     m=0
#     for v in N:
#         if type(v)==int and v>m:
#             m=v
#     # m=max(N)
#     return m
#
# r=MAXN(10,11,7,8,9,'Ajay')
# print('Max : ', r)

##Q8 Write a function to find the person eligible to vote.  Details of the person  ( name , age ,  address ) passed as argument. [ use the Arbitrary Keyword Argument ]

# def CheckV(**Voter):
#     if 'Age' in Voter.keys():
#         if Voter['Age']>=18:
#             return 'YES'
#         else:
#             return 'NO'
#     else:
#         print('Age keyword not passed for voter')
#
#
# r=CheckV(Name="Ajay", Age=19, location='gkp'); print('Status:', r)
# r=CheckV(Name="Ajay", Age=15, location='gkp'); print('Status:', r)
# r=CheckV(Name="Ajay", Age=19, location='gkp'); print('Status:', r)

##Q9 Write a function to find the sum of all the numbers only passed as argument. The function can accept the arguments of any type.
# def SUMN(*N):
#     s=0
#     for v in N:
#         if type(v)==int:
#             s=s+v
#
#     return s
#
# r=SUMN(10,20,'Ajay',30,'#rr',40,50);print('Sum: ',r)

##Q10 Write a function to find the count of numbers in the range specified below for the 10 numbers passed as argument and return result.
#
# def COUNT(*N):
#     c1=0;v1=[]
#     c2=0;v2=[]
#     c3=0;v3=[]
#     c4=0;v4=[]
#     for v in N:
#         if v <0:
#             c1=c1+1
#             v1=v1+[v]
#
#         if v>0 and v<=50:
#             c2=c2+1
#             v2=v2+[v]
#
#         if v>51 and v<=100:
#             c3=c3+1
#             v3=v3+[v]
#
#         if v>100:
#             c4=c4+1
#             v4=v4+[v]
#
#     r={'c1':[c1,v1],'c2':[c2,v2],'c3':[c3,v3],'c4':[c4,v4]}
#     # r={'c1':c1,'c2':c2,'c3':c3,'c4':c4}
#     return r
#
#
# r=COUNT(-78,89,76,62,45,67,78,92,2,-5)
# # print('Count < 0      : ', r['c1'])
# # print('Count 0-50    : ', r['c2'])
# # print('Count  51-100 : ', r['c3'])
# # print('Count > 100    : ', r['c4'])
#
# print('Count < 0      : ', r['c1'][0], r['c1'][1])
# print('Count 0-50    : ', r['c2'][0], r['c2'][1])
# print('Count  51-100 : ', r['c3'][0], r['c3'][1])
# print('Count >100    : ', r['c4'][0], r['c4'][1])
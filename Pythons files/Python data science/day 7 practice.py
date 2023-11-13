
#Q2

# s= ' Green Revolution'
# g=s[len(s):0:-1]
# print(g)

#Q3
#a)
# print( 'I like Gita\'s pink colour dress')
#it will print I like Gita's pink colour dress
#as \ is also use to print symbols inside a str

# b) 
# str='Honesty is the best policy'
# print(str.replace('o','*'))
# will replace the o with value symbol of *

# # c) 
# str='Hello World' 
# print(str.istitle( ))
# will show True if the string is a title-cased string otherwise returns False.

# # d) 
#  str="Group Discussion" 
# print (str.lstrip("Gro"))
#it will remove/strip he gro from the string

#Q4
# str="Global Warming"


# a)
# #print (str.lstrip("Grobal War"))
# g=str[len(str)-4:len(str):1]
# print(g)

# b)
# print(str[4:8:1])

# c)
# if str.isalnum():
#         print(f"{str} it is alphanumeric charater")
# else:
#         print(f"{str} is not alphanumeric charater")

# d)
# x=str.strip("ming")
# print(x)

# e)
# x=str.strip("Glob")
# print(x)

# f)
# for i in range(len(str)):
#   if str.startswith("Wa",i):
#     res=i
#     print(i)

# g)
# print(str.upper())

# h)

# if str.istitle():
#     print(str," is titled")
# else:
#     print(str,"is not titled")

# i)

# print(str.replace('a','*'))



#Q5

# str="P@#yn26at^&i5ve"
# cl=0
# cu=0
# cd=0
# cs=0

# for v in str:
#     if v.isupper():
#         cu=cu+1
#     elif v.islower():
#         cl=cl+1
#     elif v.isnumeric():
#         cd=cd+1
#     else:
#         cs=cs+1
# print(cu,cl,cs,cd)


#Q6

# X=input("Enter the Number: ")
# N=X.split(' ')
# s=0
# for v in N:
#     try:
#         s=s+eval(v)
#     except :
#         pass
# print('Sum:',s)
# print('Avg:',s/len(N))

#Q7

# S='Python is a Programming Language'
# ca=ce=ci=co=cu=0
# for v in S:
#     if v=='a' : ca=ca+1
#     if v=='e' : ce=ce+1
#     if v=='i' : ci=ci+1
#     if v=='o' : co=co+1
#     if v=='u' : cu=cu+1

# print('Count of a : ',ca)
# print('Count of  e: ',ce)
# print('Count of  i: ',ci)
# print('Count of  o: ',co)
# print('Count of  u: ',cu)

#or

# print('Count of a :', S.count('a'))
# print('Count of e :', S.count('e'))
# print('Count of i :', S.count('i'))
# print('Count of o :', S.count('o'))
# print('Count of i :', S.count('u'))

#Q8

# MainString = 'Ajay vijay Sanjay Ajay Ajit Vijay Vikas Rakesh'
# SearchString= 'Vijay Rakesh'

# for key in SearchString.split(' '):
#     count=MainString.count(key)
#     print(key, ' : ',count)

#Q9
# MainString = 'Ajay vijay Sanjay Ajay Ajit Vijay Vikas Rakesh'
# c=0
# for key in MainString.split():
#     if 'A' == key[0]:
#         c=c+1
# print('Count: ', c)


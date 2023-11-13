# #Q2
# d= { 'name' : 'Ajay', 'age' : 40, 'class':5}
# print(d.keys())
# print(d.values())

# #Q3
# T= {1:10,2:20,3:30,4:40,5:50,6:60}
# #1.
# print(len(T.keys()))
# #2.
# print(len(T.values()))
# #3.
# sm=sum(T.values())
# print(sm)
#  or
#1.
# c=0
# for c in T:
#  if c<len(T.keys()) :
#     c=c+1
#  else:
#     print(c)

# #2.
# d=0
# for d in T:
#  if d<len(T.values()) :
#     d=d+1
#  else:
#     print(d)

# #3.
# sm=0
# for i in T.values():
#     sm=sm+i
# print(sm)

# #Q4
Key = [ 'Mango', 'Banana', 'Apple']
Value = [40, 50,100]

## 1st way long and not suitable
# Fruit_Price={}
# i=0
# x=0
# j=0
# if i<len(Key):
#     if j<len(Value):
#      for x in Key:
#       for x in Value:
#         Fruit_Price[Key[i]]=Value[i]
#         # print(Fruit_Price)
#         # print(Key[i])
#         # print(Value[j]) 
#       i=i+1
#       j=j+1
#     print(Fruit_Price)
        
## or 2nd way
# d={}
# i=0
# for k in Key:
#     d[k]= Value[i]
#     i=i+1
# print(d)
##or 3rd easy way

# d=dict(zip(Key,Value))
# print(d)

##Q5.
# n= [ 11,12,13,14,15,21,22,23,24,25 ]

# d={'odd':0, 'even':0}

# for v in n:
#     if v%2==0:
#         d['even']= +1
#     else:
#          d['odd']= +1
# prinr(d)
       
##Q6.
# def Area_of_rect(width, height):
#     area = width * height
#     return area

# width = float(input("Enter the width of the rectangle: "))
# height = float(input("Enter the height of the rectangle: "))

# print("The area of the rectangle is:", Area_of_rect(width, height))

##Q7.
# def Area_of_circle(Radius):
#     PI=3.14
#     area = PI*Radius * Radius
#     return area

# n = float(input("Enter the width of the Circle: "))

# print("The area of the rectangle is: ", Area_of_circle(n))
       
##Q8.

# def factorial(n):
     
#     # return 1 if (n==1 or n==0) else n * factorial(n - 1)
#     if (n==1 or n==0):
#      return 1
#     else:
#       return n* factorial(n-1)
       
 

# num = int(input("Enter the number: "))
# print("Factorial of",num,"is",factorial(num))

##Q9.
# def Sum_of_natural(sn):
#    sn=0
#    for i in range(1,11):
#      sn=sn+i

#    print ("sum of first 10 natural numbers",sn ) 
# Sum_of_natural(11)

# def SUMN(N):
#     s=0
#     for i in range(1,N+1):
#         s=s+i
#     return s
            
##Q10
# def add_of_4(n1,n2,n3,n4):
#     add=n1+n2+n3+n4
#     return add

# n1 = int(input("Enter the 1st number : "))
# n2 = int(input("Enter the 2nd number : "))
# n3 = int(input("Enter the 3rd number : "))
# n4 = int(input("Enter the 4th number : "))
# print("The area of the rectangle is:", add_of_4(n1,n2,n3,n4))




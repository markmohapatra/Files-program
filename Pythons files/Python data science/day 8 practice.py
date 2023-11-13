# #Program uses a nested-for loop to display multiplication tables from 1-10
# for i in range(1,11): 
#  for j in range(1,11): 
#    k = i*j 
#    print (k, end=' ') 
#  print( ) 


# #Program uses a nested for loop to find #the prime numbers from 2 to 100
# i = 2 
# while(i < 100): 
#   j = 2 
#   while(j <= (i/2)): 
#     if not(i % j) : 
#        break 
#     j = j + 1 
#   if (j > i/2) : 
#     print (i, " is prime") 
#   i = i + 1 

#Q2 print out puts:
#a.
# print (type ([1,2]) )
#b.
# a= { 1, 2, 3, None, ( ), [ ]  }
# print(a)

#c.
# A= [ 1,2,3,4,5]
# L=len(A) 
# S=0 
# for I in range(1,L,2): 
#     S+=A[I] 
#     print( "Sum=",S)

#d.

# t=tuple() 
# t = t +("PYTHON",) 
# print( t )
# print (len(t) )
# t1=(10,20,30) 
# print (len(t1))

#Q3.

# #1.
# ListA = [1, 4, 3, 0]
# print(ListA) 
# #2.	
# ListB= ['x', 'z', 't', 'q'] 
# print(ListB)
# # # 3.	
# ListA.sort ( )

# # # 4.	
# print(ListA )
# # # 5.	
# ListA.insert (0, 100) 
# print(ListA )
# # # 6.	
# ListA.remove (3)
# print(ListA) 
# # # 7.	
# ListA.append (7)
# print(ListA) 
# # # 8.	
# ListC=ListA+ListB
# print(ListC)
# # # 9.	
# ListB.pop ( ) 
# print(ListB)
# # # 10.	
# ListA.extend ( [4, 1, 6, 3] )
# print(ListA)

# #Q4
# #1.
# std=['Ajay','Verma','Shara','Mari','Sam']
# #2.
# s=input("Enter the name you want to add: ")
# std.append(s)
# #3.
# print("The list you have entered is: \n",std)
# #4.
# num=int(input("Enter the name you want to add: "))
# if num<len(std):
#     print(std[num])
# else:
#     print("The number index does not exist in the list")
# #5.
# std.insert (0, 'Kamal')
# std.insert (1, 'Sanjana')
# #6.
# print("After adding Kamal and Sanjana at start, the list is: \n",std)
# #7.
# n=input("Enter the name you want to add: ")
# if n in std:
#     std.remove(n)
# else:
#     std.append(n)
# print("The updated list is:",std)
# #8.
# r=std.copy()
# r.reverse()
# #9.
# print("Original list: \n",std)
# print("Reverse list is: ",r)
# #10.
# std.pop()
# print(std)

#Q5.

# x = {"a", "b", "c"}
# y = {"c", "d", "e"}
# z = {"f", "g", "c"}

# result = x.intersection(y, z)
# print (result)

#Q6
# T1 = {10,30,50 }
# T2= {20,40,60}
# T3= T1.union(T2)
# T3=sorted(T3)
# print(T3)

#7.
# A = {"a", "b", "d", "e"}
# B = {"b", "c", "e", "f"}
# C = {"d", "e", "f", "g"}
# #(i).
# print(A.intersection(B.union(C))==(A.intersection(B)).union(A.intersection(C)))
# #(ii).
# print(A.union(B.intersection(C))==(A.union(B)).intersection(A.union(C)))

#Q8
# set1 = { 10, 20, 30, 40, 50 }
# set2 = { 30, 40, 50, 60, 70 }
# #a.
# print("identical elements in both sets are: ",set1.intersection(set2))
# #b.
# set3=set1.union(set2)
# print("All items from both set without any duplicate",set3)
# # #c.
# set4=set1.symmetric_difference(set2)
# print("set of all elements in either A or B, but not both are: ", set4)
# #d.
# set5= set1.intersection(set2)
# print("Common element",set5)



    


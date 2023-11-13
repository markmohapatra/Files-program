# x=int(input("Enter the number: "))
# sq=x*x
# cb=x*x*x
# print("\nThe square and cube of the number {0} is {1} and {2}".format(x,sq,cb))

#Q3
# x=int(input("Enter the 1st number: "))
# y=int(input("Enter the 2nd number: "))

# if(x==y):
#  print("Both numbers are equal, please enter different number")
# elif(y>x):
#  print(y,"is the greatest")
# else:
#  print(x,"is the greatest")

#or
# a=int(input("Enter the 1st number: "))
# b=int(input("Enter the 2nd number: "))

# if a>b:
#     g=a
# else:
#     g=b
# print(f"Greatest number from {a} and {b} is {g}")

#Q4
# x=int(input("Enter the number you want to check: "))
# if(x%2==0):
#     print(x,"is an even number")
# else:
#     print(x,"is an odd number")

#Q5
# x=int(input("Enter the number you want to check: "))
# if(x%7==0):
#     print(x,"is an divisible 7")
# else:
#     print(x,"is not divisible 7")

#Q6

# x=int(input("Enter the 1st number: "))
# y=int(input("Enter the 2nd number: "))
# z=int(input("Enter the 3rd number: "))

# if(x>y and x>z):
#  print(x,"is the greatest")
# elif(y>z):
#  print(y,"is the greatest")
# else:
#  print(z,"is the greatest")

#Q7

# x=int(input("Enter the number you want to check: "))
# if(x%3==0 and x%5==0):
#     print(x,"is divisible by 3 and 5")
# elif(x%3==0):
#     print(x,"is divisible by 3")
# elif(x%5==0):
#     print(x,"is divisible by 5")
# else:
#     print(x,"is not divisible by 3 or 5")

#or

# x=int(input("Enter the number you want to check: "))

# case: 1
# if(x%3==0 and x%5==0):
#  print(x,"is divisible by 3 and 5")
# case: 2
# if(x%3==0 and not(x%5==0)):
#  print(x,"is divisible by 3 but not by 5")
# case: 3
# if(not(x%3==0) and x%5==0):
#  print(x,"is divisible by 5 but not by 3")
# case: 4
# if(not(x%3==0) and not(x%5==0)):
#  print(x,"is not divisible by 3 or 5")


#Q8


# n=int(input("Enter the number you want to check: "))
 
# # if the number is positive
# if n > 0:
#     print("Positive")
         
#     # if the number is negative
# elif n < 0:
#     print("Negative")
         
#     # if the number is equal to
#     # zero
# else:
#     print("Equal to zero")

#Q9
# n=int(input("Enter the year you want to check: "))
  
# if (n % 100 == 0 and n % 400 == 0 or n%4==0):
#  print ("Year is leap.")
# else:
#  print ("Year is not leap.")

#10

# num=int(input("Enter the number you want to check: "))

# n = num
# rev = 0
# while(num>0):
#     dg = int(num % 10)
#     rev = int(rev * 10 + dg)
#     num = int(num / 10)
       
# if(n==rev):
#     print(n," is palindrome")
# else:
#     print(n," is not palindrome")

#Q11

# cp=float(input("Enter the cost price : "))
# sp=float(input("Enter the selling price : "))
# pl=sp-cp
# if (pl>0):
#     print(pl,f"is the profit of the item sold")
# else:
#     print(pl,f"is the loss of the item sold")

#Q12


# se={ "(80% <= avg)"		:"Distinction",
#  "(60% <= avg > 80%)" 	:"First Division",
#  "(45% <= avg > 60%)"	:"Second Division",
#  "(40% <= avg > 45%)" 	:"Pass",
#  "(avg > 40%)" 		:"Promotion not granted"}

# pys=float(input("Enter the physics marks: "))
# chm=float(input("Enter the chemistry marks : "))
# bio=float(input("Enter the biology marks: "))


# avg=(pys+chm+bio)/3

# if(avg >= 80):
#  print("The average of physics,chemsitry and biology is: ",avg,"and grade is:Distinction")
# elif(80> avg >= 60):
#  print("The average of physics,chemsitry and biology is: ",avg,"and grade is:First Division")
# elif(60> avg >= 45):
#  print("The average of physics,chemsitry and biology is: ",avg,"and grade is:Second Division")
# elif(45> avg >= 40):
#  print("The average of physics,chemsitry and biology is: ",avg,"and grade is:Pass")
# elif(40> avg):
#  print("The average of physics,chemsitry and biology is: ",avg,"and grade is:Promotion not granted")

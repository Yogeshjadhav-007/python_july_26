#1) print 1 to 10 using while
# i=1
# while i<=10:
#     print(i)
#     i+=1

#2) print 10 to 1
# i=10
# while i>=1:
#     print(i)
#     i-=1

#3)
# i = 2
# while i <= 20:
#     print(i)
#     i += 2

# str="Python"
# # i=0
# # for s in str:
# #     print(s,"+ve index:",i," -ve index:",i-len(str))
# #     i+=1
# print(len(str))
# print(str[0:5]) 
# print(str[-6:-1:2])
# print(str[5:0:-1])

#Q1.Accept a number from user and print its table
# num=eval((input("enter a number:")))
# i=1
# while i<=10:
#     print(num,"x",i,"=",num*i)
#     i+=1

# q2. hollow square pattern
# for i in range(5):
#     for j in range(5):
#         if i==0 or i==4 or j==0 or j==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#q3. full square star pattern
#outer loop reprensents the rows and inner loop represents the columns
# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()

#q4. left triangle star pattern
# for i in range(6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

#q5.right trinagle star pattern
# for i in range(1,6):
#     for j in range(5-i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()

#q6. inverted triangle star pattern
# for i in range(5):
#     for j in range(5-i):
#         print("*",end=" ")
#     print()

#Q7. Accept a number and print its Factorial
# num=eval(input("enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print("factorial of",num,"is",fact)

#q8.Accept name from user until its your name
# name=""
# while name!="yogesh":
#     name=input("enter your name:").strip()

#q9. print even numbers from 1 to 100
# num=int(input("enter a number:"))
# for i in range(2,num+1,2):
#     print(i)

#print odd numbers
# num=int(input("enter a number:"))
# for i in range(1,num+1,2):
#     print(i)

#print tables number that is enteres bu user 
# num=int(input("enter a number:"))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)

#print square of anumber
# num=eval(input("enter a number:"))
# num=8
# for i in range(2,num+1):
#     print(i*i)

# print sum of 1 to 50
# sum=0
# for i in range(1,51):
#     sum=sum+i
# print(sum)

# print sum of evne numbers
# sum=0
# for i in range(2,51,2):
#     print("even numbers",i)
#     sum+=i
# print("the sum of even numbers",sum)

# 2. while loop - iterates until the condition is true. it is used when user dosent know no of iterations
#print 1 to 10 numbers
# i=1
# while i<=10:
#     print(i)
#     i+=1

# # print 10 to 1 
# i=10
# while i>=1:
#     print(i)
#     i-=1







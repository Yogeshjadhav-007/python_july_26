#conditional statements
#1) if - if condition is true then its execute the block of code
# n1=eval(input("enter the number:"))
# if n1>15:
#     print("Oops! you have entered the number greater than 15")
# print("n1=",n1)
# print("end")

#2) if else - if cond is true it returns true otherwise it returns false
# age=int(input("enter your age:"))
# if age>=18:
#     print("you are eligible for voting")
# else:
#     print("not eligible")

#q1
# n1=int(input("enter the first number:"))
# n2=int(input("enter the second number:"))
# max=n1
# if n2>n1:
#     max=n2
# print("max of two number",max)
# Q2
# num=int(input("enter the number:"))
# if num>0:
#     print("positive")
# else:
#     print("negative")

# Q3
# from sys import *
# #command line arguments
# print(argv[1:])
# n1=int(argv[1])
# n2=int(argv[2])
# if n1>n2:
#     print("n1 is greater")
# else:
#     print("n2 is greater")

#ladder if-elif-else
# n1=int(input("enter the first number:"))
# n2=int(input("enter the second number:"))
# n3=int(input("enter the third number:"))
# if n1>n2 and n1>n3:
#     print("n1 is max")
# elif n2>n3:
#     print("n2 is max")
# else:
#     print("n3 is max")

#q1
# state=input("enter the state:")
# if state=="maharashtra":
#     print("mumbai")
# elif state=="goa":
#     print("panji")
# elif state=="karnataka":
#     print("banglore")
# else:
#     print("invalid state")

#q2
s1=float(input("enter marks of s1:"))
s2=float(input("enter marks of s2:"))
s3=float(input("enter marks of s3:"))
s4=float(input("enter marks of s4:"))
s5=float(input("enter marks of s5:"))
marks=s1+s2+s3+s4+s4+s5/5*100
percentage=int(input("enter the marks:"))
if marks>=75 and marks<=100:
    print("distinction")
elif marks>=60 and marks<=75:
    print("first class")
elif marks>=50 and marks<=60:
    print("second class")
elif marks>=40 and marks<=50:
    print("pass class")
elif marks<=40:
    print("fail")







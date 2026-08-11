#function with no argument and no return
# def greet():
#     print("hello")
# greet()

#even no from 1 to 20
# def even():
#     for i in range(1,21):
#         if i%2==0:
#             print(i)
#             i+=2
# even()

#print odd numbers
# def odd():
#     for i in range(1,21):
#         if i%2!=0:
#             print(i)
#             i+=1
# odd()

#accept a number print its even or odd
# def even_odd():
#     num=int(input("enter the number:"))
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd()

#Write a function that accepts a number and prints its square.
# def sqr():
#     num=eval(input("enter the number:"))
#     num=num*num
#     print(num)
# sqr()

#Write a function that accepts two numbers and prints the greater number.
# def great():
#     num1=eval(input("enter the num1:"))
#     num2=eval(input("enter the num2:"))
#     if num1>num2:
#         print("num1 is greater")
#     elif num2>num1:
#         print("num2 is greater")
#     else:
#         print("invalid number")
# great()

#Write a function that accepts a list from the user and prints the sum of all elements.
# def sum1():
#     l=eval(input("enter the list:"))
#     sum=0
#     for i in l:
#         sum=sum+i
#     print("sum=",sum)
# sum1()

#2)function with argument with no return
# def greet(name):
#     print("hello",name)
# greet("yogesh")

#even or odd
# def even_odd(num):
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd(6)

#Write a function that accepts a number and prints its square.
# def sqr(num):
#     num=num*num
#     print(num)
# sqr(3)

#Write a function that accepts two numbers and prints the greater number.
# def great(num1,num2):
#     if num1>num2:
#         print("num1 is greater")
#     elif num2>num1:
#         print("num2 is greater")
#     else:
#         print("invalid number")
# great(10,22)

##Write a function that accepts a list from the user and prints the sum of all elements.
# def total(l):
#     sum=0
#     for i in l:
#         sum=sum+i
#     print(sum)
# total([10,20,50])

#3) function with no argument and with return
# def number():
#     return 100
# x=number()
# print(x)

#Write a function with no argument and with return to return the sum of two numbers entered by the user.
# def add():
#     n1=eval(input("enter the num1:"))
#     n2=eval(input("enter the num2:"))
#     n3=n1+n2
#     return n3
# x=add()
# print(x)

#even or odd
# def even_odd():
#     num=eval(input("enter the number:"))
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
#     return 
# x=even_odd()
# print(x)

#factorial 
# def factorial():
#     num=eval(input("enter the number:"))
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     return fact
# x=factorial()
# print(x)

##Write a function that accepts a list from the user and prints the sum of all elements.
# def total():
#     sum=0
#     l=eval(input("enter the list:"))
#     for i in l:
#         sum=sum+i
#     return sum
# x=total()
# print(x)



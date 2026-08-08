#1) for loop
# str="python"
# for s in str:
#     print(s)
# i=0
# for s in str:
#     print(s,"+ve index",i,"-ve index",i-len(str))
#     i+=1

#q1
# i=0
# for i in range(1,11):
#     print(i)
#     i+=1

#q2
# i=0
# for i in range(1,10,2):
#     print(i)
#     i+=1

# l1=eval(input("enter a list"))
# for i in l1:
#     print(i)

#2) while loop
# num=int(input("enter the number:"))
# i=1
# while i<=10:
#     print(num*i)
#     i=i+1

# #3) factorial
# num = int(input("Enter a number: "))
# fact = 1
# i = 1
# while i <= num:
#     fact = fact * i
#     i = i + 1

# print("Factorial =", fact)
# #4) accept a number and print its revrese
# num = int(input("Enter a number: "))
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# print("Reverse Number =", reverse)

# 5)accept name from user run while your name was entered by user
# name=""
# while name!="yogesh":
#     name=input("enter your name:")

#3) nested loops - loops inside a loop
# for each value of outer loop inner loop gets completely exeucuted
# outer ioops= rows and inner loop=columns
#infinite loop
# while True:
#     print("loop")

# for i in range(3):
#     for j in range(2):
#         print("hello",end=" ")
#     print()

#examples
# for i in range(1,4):
#     for j in range(i):
#          print("*", end=" ")
#     print()

# for i in range(1,4):
#     for j in range(1,i+1):
#          print(j, end=" ")
#     print()

# for i in range(1,4):
#     for j in range(1,i+1):
#          print(i, end=" ")
#     print()

# for i in range(1,4):
#     print("*" *i)
# print()

#4) transfer statement 
#1)break
# i=0
# while i<5:
#     print("hello")
#     i+=1
#     break
#     print("hi")

# for i in range(20):
#     if i%2==0:
#         continue
#      print(i)


# num = [10,20,0,30,0]
# for i in num:
#     if i==0:
#         continue
#     print(100/i)

#q1 print prime or not
# n=int(input("enter the number:"))
# if n%2==0:
#     print("Not Prime")
# elif n%3==0:
#     print("Not Prime")
# elif n%5==0:
#     print("Not Prime")
# else:
#     print("Prime")

#q2
# i=1
# while i<=10:
#     if i==5:
#         i+=1
#         continue
#     print(i)
#     i+=1

#q3
# sum=0
# for i in range(1, 51):
#     sum=sum+i
# print("Sum= ",sum)

#break
# items=[10,20,700,60,70]
# for item in items:
#     if item>500:
#         print("insurance is required")
#         break
#     print(item)

# #continue
# carts=[10,20,500,700,60,70]
# for item in carts:
#     if item>=500:
#         print("can't process")
#         continue
#     print(item)

#pass
# for i in range(50):
#     if i%9==0:
#         print(i)
#     else:pass

#else with loop
# cart=[10,20,30,700,60,70]
# for item in cart:
#     if item>500:
#         print("processing is enough")
#         break
#     print(item)
# else:
#     print("congrats..all item processed")
# print("end of application")

#del
# x=10
# print(x)
# del x
# print(x)
    






        




#1) with no return wiht no argument
# n1=100 #gloabla var
# def add():
#     n1=int(input("enter the first number:"))
#     n2=int(input("enter the second number:"))
#     n3=n1+n2
#     print(n3)
# add()
# print("n1=",n1)

#2) with return and no argument
# def add():
#     n1=int(input("enter the first number:"))
#     n2=int(input("enter the second number:"))
#     n3=n1+n2
#     return n1,n2,n3
# res=add()#n1,n2,n3
# print("sum=",res)

#3) with no return with argumnet
# def add(a,b):# we can use same args like in add bcoz both address are diff
#     n3=a+b
#     print("sum=",n3)
#     n2=50 #bcoz its local var cant cahnge n2 value
#     return 
# n1=int(input("enter the first number:"))
# n2=int(input("enter the second number:"))
# add(n1,n2)
# print("n2 outside:",n2)

#4) with return and with argument
# def add(a,b):
#     return a+b
# res=add(n1,n2)
# n1=int(input("enter the first number:"))
# n2=int(input("enter the second number:"))
# print(res)

# accept string and print occurance of each letter using no return and no argumnet
def occur():
    s=input("Enter a string: ")
    d={}
    for ch in s:
        d[ch]=d.get(ch,0)+1
    for key,value in d.items():
        print(key,"occurred",value,"times")
occur()

# accept a number and prints its reverse using with return and no argument
def number():
    n=input("enter a number:")
    s=n[::-1]
    return s
res=number()
print(res)

# accept a number and prints its factorial using with no return and argument
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
num=int(input("Enter a number: "))
factorial(num)

# accept a list and print and print sum of list with return and argument
def sum_list(l):
    total=0
    for i in l:
        total=total+i
    return total
l=eval(input("enter the list:"))
res=sum_list(l)
print(res)

if ch==1:
    occur()
elif ch==2:
    res=number()
    print(res)
elif ch==3:
    num=int(input("enter a number:"))
    factorial(num)
elif ch==4:
    l=eval(input("enter a list:"))
    res=sum_list(l)
    print(l)
else:
    print("invalid choice")














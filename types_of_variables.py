#global varaibles and local varaibles
#1. global var - declared outside the function and it is access everywhere
#2. local var - declared inside the function
# a=10 #global var
# def f1():
#     a=100 #local var
#     print(a)
# def f2():
#     print(a)
# f1()
# f2()

#3. global keyword
# a=10 #global var
# def f1():
#     global a
#     a=100
#     print(a)
# def f2():
#     print(a)
# f1() #100
# f2() #100
# f2() #10
# f1() #100

#4. accessing global var
a=10
def f1():
    a=100
    print(a)
    print("global a:",globals()['a'])
f1()


#A decorator in Python is a function that adds extra functionality to another function without changing the original function's code.
#using annotation
# def decor(func):
#     def inner(name):
#         if name=="Jim":
#             print("You are not authorized person")
#         else:
#             func(name)
#     return inner

# @decor
# def greet(name):
#     print(f"{name} is an authorized person")

# greet("Tom")
# greet("Jack")
# greet("Jim")

#----function inside a function----
# def outer():
#     def inner(x,y):
#         return x+y
#     print(inner(10,20))
# outer()

#----create a ddecorator
# def decor(func):
#     def inner():
#         print("good morning")
#         func()
#     return inner
# def hello():
#     print("hello")
# hello=decor(hello)
# hello()

def mul(a,b):
    return a+b
d=mul(10,20)
print(d)
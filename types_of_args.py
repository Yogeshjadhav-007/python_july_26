#positional args - Arguments passed to a function according to their position are called positional arguments.
# def wish(name,sal):
#     print(f"{name} is earning {sal}")
# wish("yogesh",50000)

#keyword args - Arguments passed using the parameter name are called keyword arguments. order dosent matter
# first is position then keyword
# def wish(name,sal,age):
#     print(f"{name} is earning {sal} and age is {age}")
# wish(sal=30000,name="yogesh",age=22)
# wish("yogesh",name="tom",sal=50000,age=22)# error-wish() got multiple values for argument 'name'

#3.Default arguement - When a parameter is given a default value in the function definition, it is called a default argument.
# def wish(name,sal=20000,age=20):
#    print(f"{name} is earning {sal} and his age is {age}")
# wish("Tom")

#4. varaible length arguments - *args allows a function to accept any number of positional arguments.
# def show(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print(sum)
# show()
# show(10)
# show(10,20,1,25,34)

#positional with var length
# def show(n,*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     print("sum=",sum,"and",n)
# show("yogesh",10,20,30) #position will first then var length

#**kwargs allows a function to accept any number of keyword arguments.
#The values are stored in a dictionary.
# keyword var length argument
# def show(**kwargs):
#     for key,value in kwargs.items():
#         print(key,"=",value)
# show(name="yogesh",add="pune",mode="offline")

# def f(arg1,arg2,arg3=4,arg4=8):
#     print(arg1,arg2,arg3,arg4)
# f(3,2) #3 2 4 8
# f(10,20,30,40)
# f(25,50,arg4=100)#25 50 4 100
# f(arg4=2,arg1=3,arg2=4) #3 4 4 2
# f() #TypeError: f() missing 2 required positional arguments: 'arg1' and 'arg2'
# f(arg3=10,arg4=20,30,40) #positional argument follows keyword argument
# f(4,5,arg2=6) #TypeError: f() got multiple values for argument 'arg2'
# f(4,5,arg3=5,arg5=6)#f() got an unexpected keyword argument 'arg5'. Did you mean 'arg1'?

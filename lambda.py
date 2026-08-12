#lambda(anonymous) - a function that declare without any name

#normal function
# def sqr(n):
#     return n*n
# res=sqr(5)
# print(res)

#using lambda
# s=lambda n:n*n
# print("square:",s(5))

#
# m=lambda x,y:x if x<y else y
# n1=eval(input("enter the n1:"))
# n2=eval(input("enter the n2:"))
# print("minimum:",m(n1,n2))

#filter() - 
# def iseven(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# l1=[2,0,13,1,20,30]
# data=list(filter(iseven,l1))
# print(data)

#filter with lambda function
# l1=[2,0,13,1,20,30]
# data=list(filter(lambda x:x%2==0,l1))
# print(data)

# l1=['t','u','t','o','r','i','a','l']
# char=list(filter(lambda x:x !='t',l1))
# print(char)

# l1=[5,10,20,30,40,'a','x',50]
# l2=[10,40,'a']
# data=list(filter(lambda x:x not in l2,l1))
# print(data)

#map() - 
# l1=[2,3,4,5,6]
# data=list(map(lambda x:2*x,l1))
# print(data)

# l1=[1,2,3]
# l2=[4,5]
# data=list(map(lambda x,y:x*y,l1,l2))
# print(data)

#reduce() - return single value

# from functools import reduce
# l1=[10,20,30,40,50]
# # data=reduce(lambda x,y:x+y,l1)
# # print(data)
# data=reduce(lambda x,y:x*y,l1)
# print(data)

#function aliasing - for existing we give another name to same address
# def wish(name):
#     print("hello",name)
#     print("bye")
# wish("yogesh")
# greet=wish
# greet("ram")
# wish("kartik")
# print(id(wish))
# print(id(greet))

# f1=wish("raj")#function call
# print(f1)#none

#nested function - function inside another function(inner function)
def outer():
    print("start of outer function")
    def inner():
        print("this is inner function")
    # inner() print inside
    print("end of outer function")
    return inner

inn=outer()
inn() #print outside using function aliasing







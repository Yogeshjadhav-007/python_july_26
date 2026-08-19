#OOP is a programming approach where we organize a program using classes and objects.
#OOP means creating objects that contain data and functions together.
#class - class is a blueprint for creting a object
#object - object is instance of class
#self - pointing to current object

#creating a class
# class student():
#     name="yogesh"
#     age=22

# s1=student() #creating object
# print(s1.name)
# print(s1.age)

# class test():
#     def accept(self,n1,n2):
#         self.a=n1
#         self.b=n2
#     def add(self):
#         res=self.a+self.b
#         return res
#     def sub(self):
#         res=self.a-self.b
#         return res
#     def multi(self):
#         res=self.a*self.b
#         return res

# t1=test()
# x=int(input("enter the n1:"))
# y=int(input("enter the n2:"))
# t1.accept(x,y)
# s=t1.add()
# print("addition:",s)
# s1=t1.sub()
# print("substraction:",s1)
# m=t1.multi()
# print("multiplication:",m)

#self is instance varaible which can access throughout the methods
class Test:
    def accept(self):
        self.a=10
        self.b=20
        # c=100
    def display(self):
        print("a=",self.a)
        print("b=",self.b)
t1=Test()
t1.accept()
t1.display()

t2=Test()
t2.accept()
t2.display()






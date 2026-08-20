#1) instance varaible - varies from object to object every object has separate copy
# class student:
#     def __init__(self,name,course):
#         self.name=name
#         self.course=course
#     def display(self):
#         self.age=22 #declare instance var inside instance method using self
#         print("name:",self.name)
#         print("course:",self.course)
#         print("age:",self.age)
# s1=student("yogesh","python")
# s1.display()
# print(s1.__dict__)

# s2=student("raj","java")
# s2.display()
# print(s2.__dict__)


#declare var outside the class using object refernece varaible
# class student:
#     def __init__(self,name,course):
#         self.name=name
#         self.course=course
#     def display(self):
#         self.age=22 #declare instance var inside instance method using self
#         print("name:",self.name)
#         print("course:",self.course)
#         print("age:",self.age)
# s1=student("yogesh","python")
# s2=student("raj","java")
# s1.duration=" 2 months"
# print("s1 instance var:",s1.__dict__)
# print("s2 instance var:",s2.__dict__)
# s2.display()

#deleting instance var
#del outside using object varaible
# class student:
#     def __init__(self,name,course):
#         self.name=name
#         self.course=course
#     def display(self):
#         self.age=22 #declare instance var inside instance method using self
#         print("name:",self.name)
#         print("course:",self.course)
#         print("age:",self.age)
#         del self.course
# s1=student("yogesh","python")
# s2=student("raj","java")
# print("s1 instance var:",s1.__dict__)
# print("s2 instance var:",s2.__dict__)
# s1.display()
# s2.display()
# del s2.age
# print("s1 instance var:",s1.__dict__)
# print("s2 instance var:",s2.__dict__)

#2)static var - do not vary from object ot obj and one copy for all (class level)
# class test:
#     a=10
#     def __init__(self):
#         self.b=20
# print("a=",test.a)

# t1=test()
# t2=test()
# print("t1.a=",t1.a)
# print("t1.b=",t1.b)
# print("*****************")
# print("t2.a=",t2.a)
# print("t2.b=",t2.b)
# print("*****************")
# test.a=100
# print("t1.a=",t1.a)
# print("t1.b=",t1.b)
# print("instance var t1:",t1.__dict__)
# print("instance var t2:",t2.__dict__)
# print("*****************")
# test.a=200
# t2.b=500
# print("instance var t1:",t1.__dict__)
# print("instance var t2:",t2.__dict__)

#declaring stati var
# class test:
#     a=10
#     def __init__(self):
#         test.b=20
#     def instmethod(self):
#         test.c=30
#     @classmethod
#     def clmethod(cls):
#         test.d=40
#         cls.e=50
#     @staticmethod
#     def stmethod():
#         test.f=60
# print("a=",test.a)
# t1=test()
# print("b=",test.b)
# t1.instmethod()
# print("c=",test.c)
# t1.clmethod()
# print("d=",test.d)
# print("e=",test.e)
# t1.stmethod()
# print("f=",test.f)

# 
#3.Accessing static variable
class Test:
    a=10
    def __init__(self):
        #self.a=250
        print("inside constructor a=",Test.a)
        print("inside constructor using self a=", self.a)
    def inst(self):
       print("inside inst a=",Test.a)
       print("inside inst using self a=",self.a)

    @classmethod
    def clsmthd(cls):
        print("inside clsmth using cls a=",cls.a)
        print("inside clsmth using clasname=",Test.a)

    @staticmethod
    def stmthd():
        print("inside stmthd a using classname=",Test.a)

t1=Test()
t1.inst()
t1.clsmthd()
t1.stmthd()
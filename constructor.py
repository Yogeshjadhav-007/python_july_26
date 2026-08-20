#constructor - it is special method that is used to initilize instance method

#without argument
# class Test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         print("this is construtor")
#     def add(self):
#         print("addition:",self.a+self.b)

# t1=Test() #using constructor no need to call function
# t1.add()
# print("*****************")
# t2=Test()
# t2.add()

#constructor with argument
# class Test:
#     def __init__(self,n1,n2):
#         self.a=n1
#         self.b=n2
#         print("this is construtor")
#     def add(self):
#         print("addition:",self.a+self.b)

# n1=int(input("enter the first number:"))
# n2=int(input("enter the second number:"))
# t1=Test(n1,n2)
# t1.add()

#multiple constructor

# class Test:
#     def __init__(self,n1,n2): #gives error bcoz contsructor overloading is not allowed
#         self.a=n1
#         self.b=n2
#         print("this is with argumnet construtor")
#     def __init__(self):
#         self.a=10
#         self.b=20
#         print("this is construtor")
#     def add(self):
#         print("addition:",self.a+self.b)

# n1=int(input("enter the first number:"))
# n2=int(input("enter the second number:"))
# t1=Test()
# t1.add()

# class emp:
#     def __init__(self, emp_no, name, age, salary):
#         self.emp_no = emp_no
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def emp_info(self):
#         bonus = 0
#         if self.age > 50:
#             bonus = 25000
#         elif self.age >= 40 and self.age < 50:
#             bonus = 20000
#         elif self.age >= 30 and self.age < 40:
#             bonus = 15000
#         else:
#             bonus = 0

#         print("employee no:", self.emp_no)
#         print("employee name:", self.name)
#         print("employee age:", self.age)
#         print("employee salary:", self.salary)
#         print("employee bonus:", bonus)

# e1 = emp(101, "yogesh", 43, 50000)
# e1.emp_info()

# e2=emp(102,"raj",52,50000)
# e2.emp_info()

#single reference varaible multiple object
# class test:
#     def __init__(self,n1,n2):
#         self.a=n1
#         self.b=n2
#     def add(self):
#         print("addition:",self.a+self.b)
# t1=[test(10,20),test(30,40),test(50,60)]
# for obj in t1:
#     obj.add()

# class emp:
#     def __init__(self, emp_no, name, age, salary):
#         self.emp_no = emp_no
#         self.name = name
#         self.age = age
#         self.salary = salary
#         bonus=0
#         if self.age > 50:
#             bonus = 25000
#         elif self.age >= 40 and self.age < 50:
#             bonus = 20000
#         elif self.age >= 30 and self.age < 40:
#             bonus = 15000
#         else:
#             bonus = 0
#         print("employee bonus:", bonus)

#     def emp_info(self):
#         print("employee no:", self.emp_no)
#         print("employee name:", self.name)
#         print("employee age:", self.age)
#         print("employee salary:", self.salary)

# n=int(input("enter the no.of emp: "))
# emp_list=[]
# for i in range(n):
#     emp_no = int(input("enter the emp no: "))
#     name = input("enter the name: ")
#     age = int(input("enter the age: "))
#     sal = int(input("enter the salary: "))
#     e=emp(emp_no, name, age, sal)
#     emp_list.append(e)
# print("\nEmployee Details")
# for e in emp_list:
#     e.emp_info()
# e1 = emp(101, "yogesh", 32, 50000)

class employee:
    def __init__(self,eno,ename,age,sal):
        self.eno=eno
        self.ename=ename
        self.age=age
        self.sal=sal

    def details(self):
        bonus=0
        if self.age>50:
            bonus=30000
        elif self.age>40:
            bonus=25000
        elif self.age>30:
            bonus=20000
        else:
            bonus=0
        print("emp no:",self.eno)
        print("emp name:",self.ename)
        print("emp age:",self.age)
        print("emp sal:",self.sal)
        print("emp bonus:",bonus)
e1=employee(101,"yogesh",42,40000)
e1.details()

        

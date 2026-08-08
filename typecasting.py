#typecasting - converting one datatype into another

# a=12.75
# a=2+3j # error bcoz complex are not convertable
# a="12" # if we want convert string into int then there should be string is base 10 
"""a=True
x=int(a)
print("a=",a)
print("x=",x)
print("type of a:",type(a))
print("type of x:",type(x))
print(a+a)
print(x+x)"""

#convert any datatype into float
# a=True
# a=12
# a=2+3j
# a="12"
# a=False
# x=float(a)
# print("a=",a)
# print("x=",x)
# print("type of a:",type(a))
# print("type of x:",type(x))

# convert any dt into the complex
# a=True
# a=2
# a="4"
# a=False
# x=complex(a)
# print("a=",a)
# print("x=",x)
# print("type of a:",type(a))
# print("type of x:",type(x))

#converting any dt into complex using 2 args
# a=2
# b=3.2
# x=complex(a,b)
# print("x=",x)

# convert any dt into bool
#non-zero =true and 0=false
# a=5
# a=-1
#a="" #empty string
# a=" " # it conatins space so its true
# a=2+3j
# a=0+0j
# x=bool(a)
# print("a=",a)
# print("x=",x)
# print("type of a:",type(a))
# print("type of x:",type(x))

#convert any dt into sting
# a=True
# a=2
# a="4"
# a=False
# x=complex(a)
# print("a=",a)
# print("x=",x)
# print("type of a:",type(a))
# print("type of x:",type(x))

# n=13.75
# a=int(n)
# b=n-a
# print(b)

# x=[1,2,3]
# print(str(x))

emp_no=int(input("enter emp no:"))
emp_name=(input("enter emp name:"))
emp_salary=float(input("enter salary:"))
emp_address=input("enter emp address:")
married=bool(input("enter married:"))
print("emp_no:",emp_no)
print("emp_name:",emp_name)
print("emp_salary:",emp_salary)
print("emp_address:",emp_address)
print("married:",married)

# eval
data=eval(input("enter the data:"))
print(type(data))
print(data)

#argv is used to reading values that are passed from command prompt











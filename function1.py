# print("good evening")
# def display():
#     print("this is display")
#     return
# def show():
#     print("this is show")
#     display()
#     print("this is end of show")
#     return
# show()
# display()

#addition program
def add():
    n1=eval(input("enter first number:"))
    n2=eval(input("enter second number:"))
    n3=n1+n2
    print(n3)
add()    

def sub():
    n1=eval(input("enter first number:"))
    n2=eval(input("enter second number:"))
    n3=n1-n2
    print(n3)
sub() 

def areacircle():
    r=float(input("Enter the radius: "))
    area=3.14*r*r
    print("Area of Circle:",area)
areacircle()
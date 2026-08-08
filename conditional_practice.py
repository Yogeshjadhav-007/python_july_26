#1)classify persons age group
# age=eval(input("enter the age:"))
# if age>=1 and age<13:
#     print("child")
# elif age>=13 and age<=19:
#     print("teenage")
# elif age>=20 and age<=59: 
#     print("adult")
# elif age>=60:
#     print("senior")
# else:
#     print("invalid data")

#2) even or odd
# num=eval(input("enter a number:"))
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

#3) check entered number is divisible or not
# num=eval(input("enter the number:"))
# if num%9==0:
#     print("divisible by 9")
# else:
#     print("not divisible")

#4) checks case of letter
# char=(input("enter the letter:"))
# if char.isupper():
#     print("it's a uppercase character")
# elif char.islower():
#     print("it's a lowercase character")
# else:
#     print("invalid data")

#5) print largest of two numbers using only one if
# n1=int(input("enter the fisrt number:"))
# n2=int(input("enter the second number:"))
# largest=n2
# if n1>n2:
#     largest=n1
#     print("sirst number is largest")

#6).Accept marks of 5 subjects.Calculate Percentage and display the class as below:
m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))
total=m1+m2+m3+m4+m5
percentage=total/5
print("total:",total)
print("percentage:",percentage)
if percentage>=70:
    print("distinction")
elif percentage>=55:
    print("first class")
elif percentage>=45:
    print("second class")
elif percentage>=35:
    print("pass class")
else:
    print("fail")


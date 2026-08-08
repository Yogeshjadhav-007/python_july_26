#assignment op - it is used to assign the values
# a=10
# b=5
# # a=a+b
# # a+=b
# # a-=b
# # a*=b
# # a/=b
# # a%=b
# # a**=b
# print(a)

#bitwise op - Bitwise operators work on the binary form (0s and 1s) of numbers instead of the numbers directly.
# a=4
# b=5
# print(a&b)
# print(a|b)
# print(a^b)

#compliment op - The complement operator flips every bit:
# 1 becomes 0
# 0 becomes 1

# print(10>>2)
# print(10<<2)
# print(12>>2)

#special op - identity and membership
#1) identiy (is and is not)
# n1=10
# n2=10
# print("address of n1:",id(n1))
# print("address of n2:",id(n2))
# print(n1 is n2)
# print(n1 is not n2)

# l1=[10,20,"yogesh"]
# l2=[10,20,"yogesh"]
# print(l1 is l2)
# print(l1 is not l2)
# print(l1==l2)

# 2) membership op - checks particular number present or not.
# in and not in
# l1=[10,20,"python"]
# print(10 in l1)
# print(10 not in l1)

# ternary op
# a=int(input("enter any number:"))
# res="yes" if a>40 else "no"
# print(res)

#q1
# num1=int(input("enter the first number:"))
# num2=int(input("enter the second number:"))
# res="yes" if num1>num2 else "no"
# print(res)

#q2
# a=int(input("enter number1:"))
# even= "yes" if a%2==0 else "no"
# print(even)

age=int(input("enter the age:"))
res="yes" if age>=18 else "no"
print(res)







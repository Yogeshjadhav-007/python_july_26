#operators - it is used perform certain operators on operands
#1) arithmetic op
# n1=int(input("enter the first number:"))
# n2=int(input("enter the second number:"))
# n3=n1+n2
# print("addition:",n3)
# print("substraction:",n1-n2)
# print("multiplication:",n1*n2)
# print("division:",n1/n2)
# print("floor division:",n1//n2)#gives intger values but there should be both values same if ther is any
# print("modulos:",n1%n2)#gives remainder
# print("exponent:",n1**n2)

#2) relational op
# s1=10
# s2=5
# print(s1>5)
# print(s1<5)
# print(s1==s2)
# print(s1>=s2)
# print(s1<=s2)
# print(s1!=s2)

# #comparing string - string is compared on the basis of ascii codes 
# # always remember lowercase have higher ascii codes than upercase
# # ascii code (A to Z= 65 to 90) and (a to z= 97 to 122)
# # print(chr(69)) #checking ascii codes values
# r1="Python"
# r2="python"
# print(r1>r2)

#3) logical op( and, or, not)
# - and(both condition should be true)
# non boolean
# a=10
# b=20
# # c=a>5 and b true and 20
# # c=a>5 and b-50
# c=a>5 and b-20
# # c=a-10 and b
# print(c)

# if a>5 and b-20:
#     print("yes")
# else:
#     print("no") #0 consider as false

# or - atleast one condition should be true
# a=10
# b=20
# c=a<5 or b #false or 20 but in if its gives true bcoz its non zero
# print(c)

# a=10
# b=20
# c=a>b or a<b
# print(c)

# not - returns true when the condition is false and if true returns false
# a=10
# # b=not(a<50)
# b=not(a)# not(10) not(true)
# print(b)

# for string
# s1="python"
# s2=""
# s3=s1>s2 and s1<s2
# print(s3)

# cost=int(input("enter the cost ot item:"))
# sales_t=cost*12/100
# octro=cost*4/100
# e_duty=cost*2/100
# total_cost=cost + sales_t + octro + e_duty
# print("total cost of item:",total_cost)

n1=int(input("enter the laptop price:"))
n2=int(input("enter the mobile price"))
n3=int(input("enter the tv price:"))
avg=n1+n2+n3/3
print("average of all the items:",avg)



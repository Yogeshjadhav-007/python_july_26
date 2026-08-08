# """
# datatype refers to which type we are storing
# """
# #type() and id()
# # a=10
# # print("datatype of a:",type(a))
# # print("address of a:",id(a))

# #1) integer 
# """
# 4 forms of stroing integers
# binary,decimal,octal and hexa decimal
# """
# #binary - prefix 0b or 0b are allowed
# # a=0b101
# # print("a:",a)
# # print(type(a))

# #octal(o-7) - prefix 0o or 0O are allowed
# # a=0o172
# # print("a:",a)
# # print(type(a))

# #hexadecimal - prefix of 0x or 0X allowed digits 0-9 and alphabtes, a-f
# # a=0Xab24
# # print("a:",a)
# # print(type(a))

# # base conversions
# # 1) bin()
# #decimal to binary
# a=10
# print(bin(a))

# #converting hexa to binary
# a=0xab34
# print(bin(a))

# #converting ocatal to binary
# a=0o172
# print(bin(a))

# #2) octal
# #deciaml to octal
# # b=10
# # print(oct(b)) 

# # b=0x1323
# # print(oct(b)) 

# # b=0o345
# # print(oct(b)) 

# # 3) hexadeicaml
# c=10
# print(hex(c))

# c=0o122
# print(hex(c))

# c=0x442
# print(hex(c))

# c=0b1001
# print(hex(c))


#datatypes

#dict----mutable
# d={1:"Python",2:"Java",3:"DA",2:"Datascience",'a':10,"fname":"Vaishali"}
# print(d)
# print(type(d))
# print(d['fname'])

#e.frozen set  ---immutable

# s={10,20,30}
# print(s)
# print(type(s))
# fs=frozenset(s)
# print(fs)
# print(type(fs))
# fs.add(100)
# #print(fs)


#f.set -----mutable
# s=set()
# print(s)
# print(type(s))

# s={}
# print(s)
# print(type(s))

# s={10,20,"Python",True,10}
# print(s)
# print(type(s))
# #print(s[2])
# s.add("Java")
# print(s)



#e.range(n),range(n,m),range(m,n,s)   immutable

#c
# for i in range(10,0,-1):
#     print(i)

# for i in range(0,21,2):
#     print(i)

# r=range(0,20,2)
# print(r)
# for i in r:
#     print(i)


#b.
# r=range(10,51)
# print(r)
# for i in r:
#      print(i)

#a
# r=range(50)
# print(r)
# print(type(r))
# for i in r:
#     print(i)

#d.tuple---immutable

#t=10,20,30
# t=()
# print(t)
# print(type(t))


# t=(10,)
# print(t)
# print(type(t))



# t=(10,20,30,"Python",2.45,10)
# print(t)
# print(type(t))
# print(t[3])
# print(t[-1:-4:-1])
# t[0]=100




#c.list --mutable
# l=[]
# print(l)
# print(type(l))

# l1=[10,20,"Python",True,20]
# print(l1)
# print(type(l1))
# print(l1[3])
# print(l1[2:])
# l1.append(100)
# print(l1)
# l1.remove("Python")
# print(l1)


#byte and bytarray


#b bytearray --mutable

# x=[10,20,30]
# print("type(x):",type(x))
# b=bytearray(x)
# print("b=",b)
# print("type(b):",type(b))
# b[0]=100
# print("b=",b)
# for i in b:
#     print("i=",i)


#a.byte immutable

# x=[10,20,30]
# print("type(x):",type(x))
# b=bytes(x)
# print("b=",b)
# print("type(b):",type(b))
# x[0]=100
# print(x)
# # b[0]=100
# # print(b)
# print(b[2])




#list ordered
#mutable
# l1=[10,20,30]
# l2=[10,20,30]
# print("l1=",l1)
# print("l2=",l2)
# print("Address of a:",id(l1))
# print("Address of b:",id(l2))

# l1[2]=100
# print("l1=",l1)
# print("l2=",l2)
# print("Address of a:",id(l1))
# print("Address of b:",id(l2))

#****************************************************
#immutable

# a=10
# b=10
# c=25

# a="Python"
# b="Python"
# c="Java"
# print("a=",a)
# print("b=",b)
# print("Address of a:",id(a))
# print("Address of b:",id(b))
# print("Address of c:",id(c))
# b="Java"
# print("Address of a:",id(a))
# print("Address of b:",id(b))
# print("Address of c:",id(c))

# t1=(1,2,3)
# print(t1(0))

l1=[1,2,3]
print(l1[0])
l1[1]=7
print(l1)



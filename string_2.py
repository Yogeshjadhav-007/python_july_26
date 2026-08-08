
#removing spaces-rstrip(),lstrip(),strip()

# Q1.Accept State from user(Maharashtra,Goa,Karanataka)
# and print its capital

# state1=input("Enter state:")
# #state=state1.lstrip()
# #state=state1.rstrip()
# state=state1.strip()
# if state=="Maharashtra":
#     print("Capital:Mumbai")
# elif state=="Goa":
#     print("Capital:Panji")
# elif state=="Karanataka":
#     print("Capital:Bengalaru")
# else:
#     print("Invalid state")





#string comparision

# s1="Python is easy"
# s2="python"
# print(s1>s2)


#checking membership
# s1="Python is easy"
# print("easy" not in s1)


#Accessing characters by index,slicing and traversing(loop)

#using while loop
# str="Python"
# l=len(str)


# str="Python"
# i=0
# while i<len(str):
#     print(str[i])
#     i+=1

#using for loop
# str="Python"
# for x in str:
#     print(x)

# s="Learning Python is very easy"
# print(s.find("Python")) #s.find() returns the index of the first occurrence of the specified value. If the value is not found, it returns -1.
# print(s.find("java"))
# print(s.find("r"))
# print(s.rfind("r")) #s.rfind() returns the index of backward occurrence of the specified value. If the value is not found, it returns -1.

#find(substring,start,end)
# s="Learning Python is very easy"
# # x=s.find("a",12,25)
# x=s.find("a",1,10)
# print(x)

#s=aabbababa - give me all the indexes of a using find() and for loop
# s="aabbababa"
# i=0
# while i<len(s):
#     if s.find("a",i)==i:
#         print(i)
#     i+=1

# for i in range(len(s)):
#     if s.find("a",i)==i:
#         print(i)

#count() - it returns the number of occurrences of a substring in the given string.
# str="aabbabfzaba"
# print(str.count("a"))
# print(str.count("y")) #0
# print(str.count("ab"))
# print(str.count("a",3,9))

#replace() - replace old string with new string
# s="python is easy"
# s2="java"
# print(s.replace("python",s2))
# print(s2)

#split() - it splits the string into a list of substrings based on the specified delimiter (default is whitespace).
#it returns in the form list
# s="python is easy"
# s2="21/03/2034"
# l=s.split()
# l2=s2.split("/")
# print(l2)
# s3="yogesh123@gmail.com"
# l3=s3.split("@")
# print(l3)

#join() - it joins the elements of an iterable (like a list or tuple) into a single string, using a specified separator.
# str="python"
# s="@".join(str)
# print(s)

# l=["python","java","c","c++"]
# s=" ".join(l)
# print(s)

#changing cases - upper(),lower(),title(),capitalize(),swapcase()
# str="Python Is easy"
# print(str.upper())
# print(str.lower())
# print(str.title())#it converts the first character of each word to uppercase and the rest to lowercase
# print(str.capitalize())
# print(str.swapcase()) #it converts uppercase letters to lowercase and vice versa in the string.

#startawith() and endswith()
# str="python is easy"
# print(str.startswith("py"))
# print(str.endswith("sy"))
# print(str.startswith("Py")) #false bcoz its case sensitive

#isalnum ,isalpha
# s="python"
# print(s.isalnum())
# print(s.isalpha())
# print(s.isdigit())
# print(s.isupper())
# print(s.islower())
# print(s.isspace()) #returns true only when string is empty with space
# print(s.istitle())

#print all type of case by taking input from user 
# s=input("Enter a value: ")
# if s.isalpha():
#     print("Alphabet")
# if s.isupper():
#     print("Uppercase")
# if s.islower():
#     print("Lowercase")
# if s.isdigit():
#     print("Digit")
# if s.istitle():
#     print("title")
# if s.isalnum():
#     print("Alphanumeric")
# if s.isspace():
#     print("Contains only spaces")
# else:
#     print("special character")

#take user input and print alphabates but apha should be skip by 1 alpha 
#ex input=abcdefg   op=aceg
# s=input("enter the value:")
# for i in range(0,len(s),2):
#     print(s[i])

#Q1) write a program to perform following activities
#1. input= a4k3b2  ouptput= aeknb 
# s = input("Enter a string: ")
# for i in range(0, len(s), 2):
#     print(s[i], end="")
#     print(chr(ord(s[i]) + int(s[i+1])), end="")

# 2. input= a4k3b2  output= aaaakkkbb
# s=input("Enter a string: ")
# for i in range(0,len(s),2):
#     ch=s[i]
#     n=int(s[i+1])
#     print(ch*n,end="")

#3. input= abcdaaabbadeeeff  op= acbdef
# s=input("Enter a string:")
# s2=""
# for ch in s:
#     if ch not in s2:
#         s2=s2+ch
# print(s2)

#4. input= b4a1d3  op= abd134
# s=input("enter the string:")
# for ch in s:
#     if ch.isalpha():
#         print(ch,end="")
# for ch in s:
#     if ch.isdigit():
#         print(ch,end="")






















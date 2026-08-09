#set-mutable
'''
Q1.write a program to eliminate duplicates from list
Q2.Accept string and display different vowels in it
'''
# l1=[10,20,10,40,56,20]
# s=set(l1)
# print(s)

#4.set comprehension
# s={x*x for x in range(1,6)}
# print(type(s))
# print(s)


#3.membership oper
# s2={60,10,50,20,30,"Python"}
# print("Python" not in s2)

#2.Built-infunctions
#issuperset-Checks if a set contains all elements of another set.
# a = {1,2,3,4}
# b = {1,2}
# print(a.issuperset(b))

#issubset-Checks if all elements of one set are present in another set.
# a={1,2}
# b={1,2,3,4}
# print(a.issubset(b))

#isdisjoint-Checks if two sets have no common elements.
# s1={10,20,40,15}
# s2={60,70,90,100}
# print(s1.isdisjoint(s2))

#5.Mathematical operations
# e.intersection_update
# s1={10,20,30,40}
# s2={40,10,70,90}
# s1.intersection_update(s2)
# print(s1)
# s1.difference_update(s2)
# print(s2)
# s1.symmetric_difference_update(s2)

#d.symmetric_difference or ^
# s1={10,20,30,40}
# s2={40,10,70,90}
# #s3=s1.symmetric_difference(s2)
# s3=s1^s2
# print(s3)

#c.difference or -
# s1={10,20,30,40}
# s2={40,10,70,90}
# #s3=s1.difference(s2)
# s3=s1-s2
# print(s3)


#b.intersection  or &
# s1={10,20,30,40}
# s2={40,10,70,90}
# #s3=s1.intersection(s2)
# s3=s1&s2
# print(s3)
# print(s1)

#a.union  or |
# s1={10,20,30,40}
# s2={40,10,70,90}
# print(s1.union(s2))
# print(s1)
# #s3=s1.union(s2)
# s3=s1|s2
# print(s3)

#4.pop,remove,discard,clear
s={10,20,"Python",10,True}
x=s.discard(50)
print(s)

# x=s.pop()
# print("element removed:",x)
# print(s)


#3.copy
# s={10,20,30}
# #s1=s #aliasing
# s1=s.copy() #cloning
# print(s)
# print(s1)
# s.add("Python")
# print(s)
# print(s1)

#2.update
# l=[10,70,"Java"]
# s={10,20,"Python"}
# s.update(l,range(1,5))
# print(s)

#1.add
# s={10,20,'Python'}
# s.add(True)
# print(s)





#1.creating set

# d.set()
# s=set(range(1,11))
# print(s)

#set comprehension
# s={i for i in range(1,11)}
# print(s)

#convert list into set
# l1=[10,20,30,"Python"]
# s=set(l1)
# print(s)

#c.Dynamic input
# s=eval(input("Enter values for set:"))
# print(s)

#b.initialise set
# s={10,20,"Python",10,True}
# print(s)

#a.empty set
# s=set()
# print(s)
# print(type(s))
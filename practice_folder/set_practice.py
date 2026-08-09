"""
set unordered collection of elements 
duplicates are not allowed
heterogenous datatypes are allwoed
indexing are not allowed
set is mutable
"""
#creating set and empty set
# s=set()
# print(s)
# print(type(s))

# s={10,20,"python",True,30}
# print(s)
# print(type(s))

#methods of set
#1. add() - add one element in set
"""
s={10,20,"python",True,30}
x=s.add("html")
print(s)
"""
#2. update() - add multiple elements in set
"""
s={10,20,"python",True,30}
x=s.update([5,35,"css"])
print(s)

s1={1,2,3}
s2={4,5}
s1.update(s2)
print(s1)
"""
#3. remove() - removes specific elelment But if the element doesn't exist it gives error
"""s={10,20,"python",True,30}
x=s.remove(20)
print(s)"""

#4. discard() - it also removes an element but if element dosent exists it not gives error
"""s={10,20,"python",True,30}
x=s.discard(100)
print(s)"""

#5. pop() - removes and returns an random element fro set
"""s={10,20,"python",True,30}
x=s.pop()
print(x)
print(s)"""

#6. claer() - removes everything and returns empty set
"""s={10,20,"python",True,30}
x=s.clear()
print(s)"""

#membership operator - check whether element is exist or not using in and not in
"""s={10,20,"python",True,30}
print(10 in s)
print(10 not in s)"""

#set operations
#1. union(|) - all elements from both sets
s1={10,20,30,70,40,50}
s2={60,70,80,20,40}
print(s1 | s2)

#2. intersection - means common element from both side 
s1={10,20,30,70,40,50}
s2={60,70,80,20,40}
print(s1 and s2)



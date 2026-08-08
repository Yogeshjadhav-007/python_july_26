#insertion order is preserved
#mutable
#duplicates and heterogenous objects are allowed

#creating list
#empty list
# l=[]
# print(l)
# print(type(l))
# l.append("python")
# print(l)

#1) l=[10,20,"yogesh",True,2.5,[1,2]]
# print(l)

#2) create list dynamically
# l1=eval(input("enter the data:"))
# print(l1)
# print(type(l1))

#3)using split()
# s="python is easy"
# l=s.split()
# print(l)

# accessing list by indexing and slicing
# traversing - means accessing elements by using loops
# l2=[10,20,30,40,50,60,70]
# print(l2[2:5:2])
# print(l2[4::2])
# print(l2[3:6])
# print(l2[6:2:-2])
# print(l2[4:100])
# print(l2[1:-2])

# for x in l2:
#     print(x)

# i=0
# while i<len(l2):
#     print(l2[i])
#     i=i+1

# l2=[2,6,8,4,11,14,350,20]
# for i in l2:
#     if i%2==0 and i%7==0:
#         print(i)

# l=[10,20,30,40,50]
# for i in range(len(l)):
#     print("positive Index:",i,"negative Index:",i-len(l),"value:",l[i])

#built in functions
#1) count() no of occunrance any speicific number
# l1=[10,20,20,30,10]
# print(l1.count(10))
# # 2)index() - returns first occurance of number
# print(l1.index(20))
# #3)insert() insert element according to there position
# l1.insert(-2,"python")
# print(l1)

# #4) extend() extend the string
# l2=[70,80,90]
# l2.extend(l1)
# l2.extend("java")
# print(l2)

# l1 =[10,20,30]
# l2 =[30,40]
# # l1.append(l2)
# # print(l1)
# l1.extend(l2)
# print(l1)

#remove, pop and pop index
# l=[10,20,30,10,"python",True,20]
# l.remove(10) # removes the first occurance
# print(l)

# x=l.pop() # deletes the last element
# print(l)
# print("del value",x)

# l.pop(2) #removed specific position
# print(l)

# l.clear() # removes the all elements but keeps object []
# print(l)

# del l # del whole element + object
# print(l)

# del l[1]
# print(l)

# reverse,sort
# l=[10,20,30,10,"python",True,20]
# l.reverse()
# print(l)

# l=[4,10,58,34,12,5]
# # l.sort()#by default its asscending
# l.sort(reverse=True) #descending order higher to lower
# print(l)

# alising and cloning(slice and copy())
#in aliasing content and address both are same
#in cloning content is same but address is different
# l1=[10,20,30,"yogesh"]
# l2=l1
# print(l1)
# print(l2)
# print("address of l1:",id(l1))
# print("address of l2:",id(l2))
# l1[0]=100 # it affects both bcoz addrees is same
# print(l1)
# print(l2)

#2.cloning()
# l1=[10,20,30,"yogesh"]
# # l2=l1[:] slice
# l2=l1.copy()
# print(l1)
# print(l2)
# print("address of l1:",id(l1))
# print("address of l2:",id(l2))
# l1[0]=300
# print(l1)
# print(l2)

#mathmatical operations on list
# l1 =[10,20,30]
# l2 =[30,40]
# print(l1+l2)
# print(l1*3)

#comparison op
# l1 =[10,20,30]
# l2 =[30,40]
# print(l1<l2)
# l1=["python"]
# l2=["Python"]
# print(l1<l2)

#membership op
# l1 =[10,20,30]
# l2 =[30,40]
# print(10 in l1)
# print(10 not in l1))

#nested list
# l1=[10,20,[30,40,"python"]]
# print(l1[2])
# print(l1[2][2])


#list comprehension
#general way
# l=[]
# for i in range(1,11):
#     l.append(i)
# print(l)

#2. by using list comprehension
# l=[ i for i in range(1,11)]
# print(l)

#
# l1=[23,20,12,60,19,54,9]
# l2=[i for i in l1 if i%2==0]
# print(l2)

# l1=[x*x for x in range(1,6) ]
# print(l1)

#number that are present in l1 but not in l2 in general way
# l1 = [10, 20, 30, 40]
# l2 = [30, 40, 50, 60]
# l3=[]
# for i in l1:
#     if i not in l2:
#         l3.append(i)
# print(l3)

# l3 = [i for i in l1 if i not in l2] #using list comprehension
# print(l3)

# l1="python is easy"
# l2=l1.split()
# for l2 in l2:
#     print(l2,"=",len(l2))

#list comprehenisnons
# vowels=['a','e','i','o','u']
# word=input("enter the words to search the vowels:")
# found=[]
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# print(found)
# print("diff vowels present in",word,"are",found)


    
    














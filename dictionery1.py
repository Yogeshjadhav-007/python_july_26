#dictionary --mutable
#2.accessing values
# d={101: 'Python', 201: 'Java', 301: 'Da'}
# #print(d[3])
# for k in d:
#     print(k,"--",d[k])

#upadate dict
# d={101: 'Python', 201: 'Java', 301: 'Da'}
# d[201]='data science'
# d[203]='c language'
# print(d)

#deleting dictionery
# del d
# print(d)

#clear () is used to remove all the elements from dict but keeps strut

#get() if there is no key it returns none
#get(key,default) if there is no key it returns any message that provide by user 0 or int.
# d={101: 'Python', 201: 'Java', 301: 'Da'}
# # x=d.get(101)
# x=d.get(100,"error") 
# print(x)

#pop() and popitem()
# d={101: 'Python', 201: 'Java', 301: 'Da'}
# x=d.pop(101) #it removes specific element
# print(x)
# print(d)
# x=d.popitem() # it removes random element
# print(x)
# print(d)

#keys ,items and values
d={101: 'Python', 201: 'Java', 301: 'Da'}
# x=d.keys()
# print(x)
# for k in d.keys(): #print one by one
#     print(k)

#values()
# d={101: 'Python', 201: 'Java', 301: 'Da'}
# x=d.values()
# print(x)
# for v in d.values():
#     print(v)

#items() returns both keys and values
# d={101: 'Python', 201: 'Java', 301: 'Da'}
# x=d.items()
# print(x)
# for k,v in d.items():
#     print(k,"--",v)

# d1={101: 'Python', 201: 'Java', 301: 'Da'}
# d2=d1 #aliasing
# d2=d1.copy() #cloning
# d1[101]="c"
# print(d1)
# print(d2)

#setdefault() - it adds an element and if key is same it remains unchange
# d1={101: 'Python', 201: 'Java', 301: 'Da'}
# x=d1.setdefault(104,"ds")
# print(d1)

#update()
# d1={1:"apple",2:"grapes"}
# d2={3:"mango"}
# d2.update(d1)
# print(d2)

#dictionary comprehension
# d={x:x*x for x in range(1,6)}
# print(d)
# print(type(d))

#accept dictionary and print its sum
# d=eval(input("enter the dictionary:"))
# total=sum(d.values())
# print("Sum of values =",total)

#enter any word from user print its occurance
# word=input("Enter any word: ")
# d={}
# for ch in word:
#     d[ch]=d.get(ch, 0)+1
# for key,value in d.items():
#     print(key,"occurred",value,"times")

#count of vowels
# word=input("Enter any word: ")
# d={}
# for ch in word:
#     if ch in "aeiouAEIOU":
#         d[ch]=d.get(ch, 0)+1
# for key,value in d.items():
#     print(key,"occurred",value,"times")











# d[1]="Data science"
# print(d)

#1.create dictionary
#dictionary from tuple (dict())
# l=[(1,"Python"),(2,"Java"),(3,"Da")]
# d=dict(l)
# print(d)

#c.dynamic input
# d=eval(input("enter data for dictionary:"))
# print(d)

#b.intialise
# d={1:"Python",'a':'Apple',"Name":"Vaishali",1:"Java"}
# print(d)

#a.empty dict
# d={}
# print(type(d))
# print(d)
# d[1]="Python"
# d[2]="Java"
# print(d)




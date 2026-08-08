#tuple is immuatbale
#insertion order is preserved hence indexing is allowed
#heterogenous data is allowed

#empty tuple
# t=()
# print(t)
# print(type(t))

#initilaize
# t=(10,20,30,"pyton",(60,70))
# print(t[1])
# print(t[4][0])

#dynamic input
# data=eval(input("enter the tuple:"))
# print(data)

#single value tuple
# t=(10,)
# print(t)
# print(type(t))

#accessing tuple by ind, slie or traversing
# t=(10,20,"python",200,True)
# print(t[2])
# print(t[::-1])
# for x in t:
#     print(x)

#count(),sort(),min and max()
# t=(10,20,10,30,10,50)
# print(t.count(10))
# print(sorted(t))
# print(min(t))
# print(max(t))
# print(sorted(t,reverse=True))#desc order

#packing and unpacking
# a=10
# b=20
# c=30
# t=a,b,c
# print(t) packing

# t=10,20,30
# a,b,c=t
# print(a,"/t",b,"/t",c)

#square of 1 to 10
# t=(x*x for x in range(1,11))
# print(t)
# print(type(t))
# for i in t:
#     print(i)

#accept tuple from user and print its total and avg
# num=eval(input("enter list of number:"))
# total=sum(num)
# avg=sum(num)/len(num)
# print("sum:",total)
# print("average",avg)

#mathematical opertaions
# t1=(10,20,30)
# t2=(40,50)
# print(t1+t2)#concatination
# print(t1*3)#repeatation





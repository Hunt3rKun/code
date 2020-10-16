import random

list=[]
for i in range(0,20):
    list.append(random.randint(1,10))
tuple1 = tuple(list)
set1 = set(list)
print(tuple1)
for x in set1:
    print("%d出现了%d次"%(x,tuple1.count(x)))
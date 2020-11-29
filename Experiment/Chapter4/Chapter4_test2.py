import random
list_1=[]
for i in range(0,10):
    list_1.append(random.randint(1,100))
print(list_1)
list_1=[x**2 for x in list_1 if x%2!=0]+[x**3 for x in list_1 if x%2==0]
print(list_1)
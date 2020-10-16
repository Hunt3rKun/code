list=[3,8,11,26,47]
a=int(input("Please input a number:"))
list.append(a)
print(list)
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j] = list[j],list[i]
print(list)

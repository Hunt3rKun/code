list0 = [1,2,3,4,5,6,7,8,9,10]
list1 = []
list2 = []
def IsEvenFunc(n):
    return n%2 ==0
def NotEvenFunc(n):
    return n%2 !=0
list1 = list(filter(IsEvenFunc,list0))      # 奇数
list2 = list(filter(NotEvenFunc,list0))     # 偶数
list3 = []
for i in range(0,4):
    for j in range(0,4):
        if i == j:
            temp = list1[i] *10+list2[j]
            list3.append(temp)

print(list2)
print(list1)
print(list3)
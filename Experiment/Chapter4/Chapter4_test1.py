list1 = [1,2,3,4]
list2 = ['a','b','c','d']

def listSum1(a,b):
    return a + b
def listSum2(a,b):
    for item in b:
        a.append(item)
    return a
print(listSum1(list1,list2))
print(listSum2(list1,list2))

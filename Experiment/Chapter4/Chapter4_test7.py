set1 = {2, 5, 9, 1, 3}
set2 = {3, 6, 8, 2, 5}
#(1)
set1.add(7)
print("添加一个新元素7：", set1)
#(2)
print("set1和set2的并集为：", set1 | set2)
#(3)
print("set1和set2的交集为：", set1 & set2)
#(4)
print("set1和set2的交集为：", set1 - set2)
#(5)
print("4 is in set1?", 4 in set1)
print("4 is in set2?", 4 in set2)

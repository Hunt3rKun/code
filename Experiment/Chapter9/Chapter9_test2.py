import random
import numpy as np

list_random = []
for i in range(20):
    list_random.append(str(random.randint(1,100)))
with open('sjs.txt','w') as f:
    for str in list_random:
        f.write(str)
        f.write('\n')
    f.close()
arr = []
with open('sjs.txt','r') as fp:
    string = fp.readlines()
    for item in string:
        arr.append(int(item))
    fp.close()

arr_std = np.std(arr,ddof=1)
print("标准方差为:%f" % arr_std)
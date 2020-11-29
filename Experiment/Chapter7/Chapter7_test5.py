import random

import numpy as np
list = []
for i in range(12):
    list.append(random.randint(1,100))

array = np.array(list).reshape(3,4)
print(array)


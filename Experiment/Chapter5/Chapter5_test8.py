from gmpy2 import *

def isGDBH(num):
    list = []
    for i in range(1,int(num/2)+1):
        if is_prime(i):
            for j in range(int(num/2),num):
                if is_prime(j) and (num == i + j) :
                    # print(num,i,j)
                    s = str(num) + '=' + str(i) + '+' + str(j)
                    list.append(s)
    return list

print(isGDBH(10))

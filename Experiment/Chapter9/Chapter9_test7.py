import pickle

a = 10
b = 'hello'
c = [1,2]
d = (3,4)
e = {'name':'yk'}
f = {'abc','4'}
data = [a,b,c,d,e,f]

with open('bFile.dat','wb') as pk:
    for i in data:
        pickle.dump(i,pk)
    pk.close()

with open('bFile.dat','rb') as p:
    for i in range(len(data)):
        data1 = pickle.load(p)
        print("data:",data1)
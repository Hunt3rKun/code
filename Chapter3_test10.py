a=0.01
s =0
for i in range(1,31):
    s=s+100000
    x1=2*a
    a=x1
print("富翁赚的钱:{:.2f}，陌生人赚的钱:{:.2f}".format(s,a))

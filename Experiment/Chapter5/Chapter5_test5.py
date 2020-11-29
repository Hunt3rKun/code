def fuc1(n):
	sum=0
	for i in range(1,int(n/2)+1):
		sum=sum+1/(2*i)
	print(sum)
def fuc2(n):
	sum=0
	for i in range(1,int((n+1)/2)+1):
		sum=sum+1/(2*i-1)
	print(sum)
n=int(input("请输入："))
if(n%2==0):
	fuc1(n)
else:
	fuc2(n)
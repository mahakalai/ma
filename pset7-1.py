n,x=map(int,input().split())
l=[int(x) for x in input().split()]
c=0
for i in range(0,len(l)):
	sum=l[i-1]+l[i]
	if sum==x:
		c=c+1
if c==0:
	print("no")
else:
	print("yes")

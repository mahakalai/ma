k=int(input())
l=[int(x) for x in input().split()]
c=0
l1=[]
for i in range(0,len(l)):
	if l[i]==i:
		l1.append(l[i])
		c=c+1
if c==0:
	print("-1")
else:
	for i in range(0,len(l1)-1):
		print(l1[i],end=" ")
	print(l1[-1])	
	    

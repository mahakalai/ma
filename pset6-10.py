s,a=map(str,input().split())
l1=list(s)
l2=list(a)
c=0
for i in range(0,len(l1)):
	if l1[i]==l2[i]:
		c=c+1
if c==0:
	print("no")
else:
	print("yes")

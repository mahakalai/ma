k=int(input())
l=[int(x) for x in input().split()]
l.sort()
l.reverse()
c=0
for i in range(0,len(l)):
	if l[i]==0:
		c=c+1
if len(l)==c:
	print("0")
else:
	for i in range(0,len(l)):
		print(l[i],end="")
	

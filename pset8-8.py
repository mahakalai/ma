n,k=map(int,input().split())
l=[int(x) for x in input().split()]
l1=[int(x) for x in input().split()]
for i in range(0,len(l1)):
	m=l1[i]
	l.append(m)
l.sort()
for i in range(0,len(l)-1):
	print(l[i],end=" ")
print(l[-1])	
	
	

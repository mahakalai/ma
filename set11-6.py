a,b=map(str,input().split())
l=[int(x) for x in input().split()]
l1=[]
for i in range(0,len(l)):
	if l[i]%2==1:
		l1.append(l[i])
c=int(b)
print(l1[c-1])

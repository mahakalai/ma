n=int(input())
l=[int(x) for x in input().split()]
l1=[int(x) for x in input().split()]
l2=[]
for i in range(0,len(l)):
	for j in range(0,len(l1)):
		if l[i]==l1[j]:
			l2.append(l[i])
l3=list(set(l2))
l3.sort()
for i in range(0,len(l3)-1):
     print(l3[i],end=" ")
print(l3[-1])

    

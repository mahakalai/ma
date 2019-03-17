n=int(input())
l=[int(x) for x in input().split()]
m=l[0]%2
if m==0:
	for i in range(0,len(l)):
		if l[i] % 2 ==1:
			print(l[i])
else:
	for i in range(0,len(l)):
		if l[i] % 2 ==0:
			print(l[i])

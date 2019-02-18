n=int(input())
l=[int(x) for x in input().split()]
l1=sorted(l)
if l==l1:
	print("yes")
else:
	print("no")

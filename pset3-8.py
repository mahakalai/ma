s=input()
l=list(s)
for i in range(0,len(l)-1):
	if l[i]==" ":
		l.remove(l[i])
l1="".join(l)
print(l1)

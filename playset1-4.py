d=input()
l=list(d)
a="."
l.append(a)
for i in range(0,len(l)-1):
	print(l[i],end="")
print(l[-1])	

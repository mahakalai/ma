z=input()
l=[]
for i in range(0,len(z)):
	if z[i].islower():
		n=z[i].upper()
		l.append(n)
	else:
		n=z[i].lower()
		l.append(n)
s1="".join(l)		
print(s1)

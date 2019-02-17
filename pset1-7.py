s=input()
l=[]
for i in range(0,len(s)):
	if i%2==0:
		l.append(s[i+1])
	else:
		l.append(s[i-1])
for i in range(0,len(l)-1):
	print(l[i],end="")
print(l[-1])	

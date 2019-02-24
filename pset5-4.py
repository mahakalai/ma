s,k=map(str,input().split())
n=int(k)
l=list(s)
for i in range(0,n):
	a=l.pop()
	l.insert(0,a)
s1="".join(l)
print(s1)

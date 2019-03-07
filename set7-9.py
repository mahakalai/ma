n,k=map(int,input().split())
l=[int(x) for x in input().split()]
m=len(l)-k
for i in range(0,m-1):
   print(l[i],end=" ")
print(l[m-1])

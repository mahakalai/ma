n=int(input())
l=[int(x) for x in input().split()]
l2=[]
for i in range(0,len(l)):
     if l[i]<n:
        l2.append(l[i])
for i in range(0,len(l2)-1):
      print(l2[i],end=" ")
print(l2[-1])

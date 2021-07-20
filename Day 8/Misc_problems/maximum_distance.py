n=int(input())
coordx=[int(x) for x in input().split()]
coordy=[int(x) for x in input().split()]

ans=0
for i in range(n):
    for j in range(n):
        ans=max((coordx[i]-coordx[j])**2+(coordy[i]-coordy[j])**2,ans)
print(ans)


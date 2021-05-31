#Problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=894
import sys
sys.stdin=open("planting.in","r")
sys.stdout=open("planting.out","w")
n = int(input())
degree=[1]*(n+1)

for i in range(n-1):
    a,b=map(int,input().split())
    degree[a]+=1
    degree[b]+=1

ans=0
for i in degree:
    ans=max(ans,i)

print(ans)

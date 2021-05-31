#Problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=940
import sys
sys.stdin=open("factory.in",'r')
sys.stdout=open("factory.out",'w')

n = int(input())
adj=[[]]*(n+1)
vis=[False]*(n+1)

def dfs(node: int):
    vis[node]=True
    for i in adj[node]:
        if(not vis[i]):
            dfs(i)

for i in range(n-1):
    a,b=map(int,input().split())
    adj[b].append(a)

for i in range(1,n+1):
    dfs(i)
    ok=True
    for j in range(1,n+1):
        if(not vis[j]):
            ok=False
            break
    if(ok):
        print(i)
        sys.exit()
    for j in range(1,n+1):
        vis[j]=False

print(-1)

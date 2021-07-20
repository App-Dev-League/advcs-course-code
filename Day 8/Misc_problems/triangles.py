import sys 
sys.stdin=open("triangles.in","r")
sys.stdout=open("triangles.out","w")

n=int(input())
x=[0]*n
y=[0]*n

for i in range(n):
    coord=[int(i) for i in input().split()]
    x[i]=coord[0]
    y[i]=coord[1]
def solve(p:int,q:int,r:int):
    global x
    global y
    area=0
    if(x[p]==x[q] and y[p]==y[r]):
        area=abs(y[p]-y[q])*abs(x[r]-x[p])
    if(x[r]==x[q] and y[p]==y[q]):
        area=abs(y[r]-y[q])*abs(x[p]-x[q])
    if(x[r]==x[q] and y[p]==y[r]):
        area=abs(y[r]-y[q])*abs(x[r]-x[p])
    return area
ans=0
for i in range(n):
    for j in range(n):
        for r in range(n):
            ans=max(ans,solve(i,j,r))
print(ans)
            

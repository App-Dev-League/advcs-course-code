import sys 
sys.stdin=open("teleport.in","r")
sys.stdout=open("teleport.out","w")
a,b,x,y=map(int,input().split())

if(a>b):
    a,b=b,a
if(x>y):
    x,y=y,x

norm_dist=abs(a-b)
teleport_dist=abs(x-a)+abs(b-y)
ans=min(norm_dist,teleport_dist)
print(ans)



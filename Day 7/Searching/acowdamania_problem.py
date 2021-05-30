#problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=1136
import math

def check(num:int):
	give=0
	for i in range(num):
		give+=max(num-arr[i],0)
	return num-arr[num-1]<=k and give<=l*k

n,k,l=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
lo=0
hi=n
while(lo<hi):
	mid=math.ceil((lo+hi)/2)
	if(check(mid)):
		lo=mid
	else:
		hi=mid-1
print(hi)

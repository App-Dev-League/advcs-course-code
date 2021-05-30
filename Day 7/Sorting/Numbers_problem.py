#Problem: https://cses.fi/problemset/task/1621
n=input()
arr=list(map(int,input().split()))
ans=1
arr.sort()
for i in range(1,len(arr)):
	if(arr[i]!=arr[i-1]):
		ans+=1
print(ans)

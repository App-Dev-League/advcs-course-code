#Problem: https://cses.fi/problemset/task/1621

#this problem can be better solved with a set, but I feel it is a good problem for showing sorting
#however, this method does save memory if you're into that stuff 🤔🤓
n=input()
arr=list(map(int,input().split()))
#We keep the answer at one because we don't count if the first value is different
ans=1
#We sort because it can help us keep track of how many different numbers there are
arr.sort()
for i in range(1,len(arr)):
	#Since all the equal numbers will be next to each other, we can just add 
	if(arr[i]!=arr[i-1]):
		ans+=1
print(ans)

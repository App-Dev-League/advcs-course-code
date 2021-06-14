#problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=1136
import math

def check(num:int):
	#this variable counts the total amount of times we need to cite each source until we get the desired h-value
	give=0
	for i in range(num):
		give+=max(num-arr[i],0)
	#Since each paper can be cited once, the paper that has been cited the least and is needed for the desired h-value has to need less citations than the number
	#papers it can be cited in
	#the give variable has to be less than the total number of citations
	#if num passes these two conditions, then it can be a possible h-value
	return num-arr[num-1]<=k and give<=l*k

n,k,l=map(int,input().split())
arr=list(map(int,input().split()))
#We sort the array so that we can iterate through and find the papers that have been cited the most
arr.sort(reverse=True)
lo=0
hi=n
#we binary search to keep trying each h-value from 1 to n since n is the maximum possible h-value
while(lo<hi):
	mid=math.ceil((lo+hi)/2)
	if(check(mid)):
		lo=mid
	else:
		hi=mid-1
print(hi)

#Problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=963
#this is basic simulation which is pretty good for beginners. However, it's a bummy problem with an annoying impletation. 😤🥸😑
import sys
sys.stdin=open("gymnastics.in", "r")
sys.stdout=open("gymnastics.out", "w")
k,n=map(int,input().split())
ses=[[]]*k
place1=-1
place2=-1
ans = 0

#this function tests how many times cow a has lost to cow b
def check(a: int, b:int):
	cnt=0
	#we iterate all the arrays
	for i in range(k):
		#we complete search to find the places of cows a and b
		for j in range(n):
			global place1
			global place2
			if(ses[i][j]==a):
				place1=j
			if(ses[i][j]==b):
				place2=j
		#if cow a has lost to cow b, then we add 1 to the count
		if(place1<place2):
			cnt+=1
	#if cow b has beaten cow a in all of the races, then we add 1 to the answer
	if(cnt==k):
		global ans
		ans+=1

for i in range(k):
	ses[i]=list(map(int,input().split()))
#we iterate through all possible pairs of the cows
for i in range(n):
	for j in range(n):
		check(i+1, j+1)
		

print(ans)

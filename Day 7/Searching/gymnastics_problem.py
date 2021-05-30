#Problem: http://www.usaco.org/index.php?page=viewproblem2&cpid=963
import sys
sys.stdin=open("gymnastics.in", "r")
sys.stdout=open("gymnastics.out", "w")
k,n=map(int,input().split())
ses=[[]]*k
place1=-1
place2=-1
ans = 0

def check(a: int, b:int):
	cnt=0
	for i in range(k):
		for j in range(n):
			global place1
			global place2
			if(ses[i][j]==a):
				place1=j
			if(ses[i][j]==b):
				place2=j
		if(place1<place2):
			cnt+=1
	if(cnt==k):
		global ans
		ans+=1

for i in range(k):
	ses[i]=list(map(int,input().split()))

for i in range(n):
	for j in range(n):
		check(i+1, j+1)
		

print(ans)

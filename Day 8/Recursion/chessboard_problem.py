#Problem: https://cses.fi/problemset/task/1624
#Probably the best example there is for backtracking
#very good problem 🥳🤑
board=[""]*8
ans=0

def solve(num=0,rep=[]):
	#if num==8, then we have a solution
	if(num==8):
		global ans
		ans=ans+1
	else:
		for i in range(8):
			#can't have a queen on a *
			if(board[num][i]=='*'):
				continue
			else:
				check=True
				#check through the list and see the queen placed lines up with anything
				for j in range(len(rep)):
					if(i==rep[j]):
						check=False
					elif(num-j==abs(i-rep[j])):
						check=False
				#if the queen is in a good location, then we can move on
				if(check):
					rep.append(i)
					solve(num+1,rep)
					rep.pop()

board=[input() for i in range(8)]
solve()
print(ans)


#Problem: https://cses.fi/problemset/task/1624
board=[""]*8
ans=0

def solve(num=0,rep=[]):
	if(num==8):
		global ans
		ans=ans+1
	else:
		for i in range(8):
			if(board[num][i]=='*'):
				continue
			else:
				check=True
				for j in range(len(rep)):
					if(i==rep[j]):
						check=False
					elif(num-j==abs(i-rep[j])):
						check=False
				if(check):
					rep.append(i)
					solve(num+1,rep)
					rep.pop()

board=[input() for i in range(8)]
solve()
print(ans)

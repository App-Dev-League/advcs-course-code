def dfs_adjlist(node: int):
  vis[node]=True
  for i in adj_list[node]:
    if(not vis[i]):
    	dfs_adjlist(i)

def dfs_adjmat(node:int):
	vis[node]=True
	for i in range(n):
		if(adj_mat[node][i] and (not vis[i])):
			dfs_adjmat(i)

n=int(input())
vis=[False]*n
adj_list=[[]]*n
adj_mat=[[False for i in range(n)]]*n

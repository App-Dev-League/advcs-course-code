#I think you know what going on here
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

def dfs_tree(node:int, parent:int):
    vis[node]=True
    for i in adj[node]:
	if(i!=parent):
	    dfs(i,node)
	
n=int(input())
vis=[False]*(n+1)
adj_list=[[]]*(n+1)
adj_mat=[[False]*(n+1)]*(n+1)

def dfs(g,v,visited):
	visited[v] = True
	print(v,end =' ')
	for i in g[v]:
		print(visited[i],end=' ')
		if not visited[v]:
			dfs(g,i,visited)
g =[
	[],
	[2,3,8],
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7],
]

visited = [False] * 9

dfs(g,1,visited)

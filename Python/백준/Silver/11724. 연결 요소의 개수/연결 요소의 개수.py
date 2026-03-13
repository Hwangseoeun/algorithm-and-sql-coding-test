import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
edge = [[] for _ in range(N)]

for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    
    edge[node1-1].append(node2-1)
    edge[node2-1].append(node1-1)

visited = [False] * N
count = 0

def dfs(node):
    if visited[node]:
        return
    
    visited[node] = True
    
    for e in edge[node]:
        if not visited[e]:
            dfs(e)

for i in range(N):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
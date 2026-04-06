import sys

sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, input().split())

nodes = [[] for _ in range(N+1)]
visited = [False] * (N+1)
visited[0] = True
result = [0] * (N+1)
count = 0

def dfs(node):
    global count
    
    count += 1
    visited[node] = True
    result[node] = count
    
    for n in nodes[node]:
        if not visited[n]:
            dfs(n)

for i in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    
    nodes[node1].append(node2)
    nodes[node2].append(node1)

for i in range(1, N + 1):
    nodes[i].sort(reverse=True)

dfs(R)

for i in range(1, len(result)):
    print(result[i])
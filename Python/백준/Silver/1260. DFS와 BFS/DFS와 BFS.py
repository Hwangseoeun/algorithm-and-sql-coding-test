from sys import stdin
from collections import deque

N, M, V = map(int, input().split())

node = [[] for _ in range(N + 1)]

for i in range(M):
    node1, node2 = map(int, stdin.readline().split())
    
    node[node1].append(node2)
    node[node2].append(node1)

for i in range(1, N + 1):
    node[i].sort()

visited_dfs = [False] * (N + 1)
visited_dfs[0] = True

visited_bfs = [False] * (N + 1)
visited_bfs[0] = True

def dfs(num):
    visited_dfs[num] = True
    print(num, end=' ')
    
    for next_node in node[num]:
        if not visited_dfs[next_node]:
            dfs(next_node)

def bfs():
    arr = deque()
    
    visited_bfs[V] = True
    arr.append(V)
    
    while arr:
        num = arr.popleft()
        print(num, end=' ')
        
        for i in range(len(node[num])):
            if not visited_bfs[node[num][i]]:
                visited_bfs[node[num][i]] = True
                arr.append(node[num][i])

dfs(V)
print()

bfs()
print()
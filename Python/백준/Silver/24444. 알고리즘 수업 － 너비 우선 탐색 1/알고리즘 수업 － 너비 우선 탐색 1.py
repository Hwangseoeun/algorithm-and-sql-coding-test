import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, input().split())

nodes = [[] for _ in range(N+1)]
result = [0] * (N+1)
count = 0

def bfs(node):
    global count

    stack = deque()
    visited = [False] * (N+1)
    
    stack.append(node)
    visited[node] = True
    
    while stack:
        recent = stack.popleft()
        
        count += 1
        result[recent] = count
        
        for n in nodes[recent]:
            if not visited[n]:
                stack.append(n)
                visited[n] = True
    

for i in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    
    nodes[node1].append(node2)
    nodes[node2].append(node1)

for i in range(1, N + 1):
    nodes[i].sort()

bfs(R)

for i in range(1, len(result)):
    print(result[i])
from sys import stdin
from collections import deque

N, M, K, X = map(int, input().split())

city = [[] for i in range(N+1)]

for i in range(M):
    A, B = map(int, stdin.readline().split())
    
    city[A].append(B)

visited = [-1] * (N+1)

def bfs(start):
    stack = deque()
    stack.append(start)
    visited[start] += 1
    
    while stack:
        recent = stack.popleft()
        
        for c in city[recent]:
            if visited[c] == -1:
                stack.append(c)
                visited[c] = visited[recent] + 1

bfs(X)

result = []

for i in range(1, N+1):
    if visited[i] == K:
        result.append(i)

if not result:
    print(-1)
else:
    for r in result:
        print(r)
from sys import stdin
from collections import deque

V = int(input())

tree = [[] for _ in range(V)]

for i in range(V):
    temp = list(map(int, input().split()))
    node1 = temp[0] - 1
    
    for j in range(1, len(temp), 2):
        if temp[j] == -1:
            continue
        
        node2 = temp[j] - 1
        length = temp[j+1]
        
        if node1 < node2:
            tree[node1].append((node2, length))
            tree[node2].append((node1, length))

def bfs(start_node):
    visited = [False] * V
    stack = deque()
    
    stack.append((start_node, 0))
    visited[start_node] = True
    
    max_length = 0
    farthest_node = start_node
    
    while stack:
        recent_node, recent_total_length = stack.popleft()
        
        for next_node, next_length in tree[recent_node]:
            if not visited[next_node]:
                next_total_length = recent_total_length + next_length
                stack.append((next_node, next_total_length))
                visited[next_node] = True
                
                if max_length < next_total_length:
                    max_length = next_total_length
                    farthest_node = next_node
    
    return farthest_node, max_length

node_A, length_A = bfs(0)
node_B, length_B = bfs(node_A)

print(length_B)
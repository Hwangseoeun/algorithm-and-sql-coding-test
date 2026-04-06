from sys import stdin
from collections import deque

computer_cnt = int(input())
net_cnt = int(input())

computers = [[] for _ in range(computer_cnt + 1)]
count = 0

def bfs():
    global count
    
    stack = deque()
    visited = [False] * (computer_cnt + 1)
    
    stack.append(1)
    visited[1] = True
    
    while stack:
        recent = stack.popleft()
        
        for i in computers[recent]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                count += 1
    

for i in range(net_cnt):
    com1, com2 = map(int, stdin.readline().split())
    
    computers[com1].append(com2)
    computers[com2].append(com1)

bfs()

print(count)
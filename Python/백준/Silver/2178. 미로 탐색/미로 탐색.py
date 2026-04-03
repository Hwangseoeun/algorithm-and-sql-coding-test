from sys import stdin
from collections import deque

N, M = map(int, input().split())
board = [] * N

for i in range(N):
    board.append(list(map(int, stdin.readline().strip())))

visited = [[False] * M for _ in range(N)]
count = [[0] * M for _ in range(N)]
directions = [[-1,0], [0,1], [1,0], [0,-1]]

def dfs():
    global count, visited
    
    arr = deque()
    arr.append((0,0))
    visited[0][0] = True
    count[0][0] = 1
    
    while arr:
        current_x, current_y = arr.popleft()
        
        for x, y in directions:
            next_x = current_x + x
            next_y = current_y + y
            
            if next_x >= 0 and next_y >= 0 and next_x < N and next_y < M:
                if not visited[next_x][next_y] and board[next_x][next_y] == 1:
                    arr.append((next_x, next_y))
                    visited[next_x][next_y] = True
                    count[next_x][next_y] = count[current_x][current_y] + 1

dfs()
print(count[N-1][M-1])
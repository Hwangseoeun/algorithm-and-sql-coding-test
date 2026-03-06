from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0
direction = [[0,1], [-1,0], [0,-1], [1,0]]

empty = []

def get_wall_combi():
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 0:
                empty.append((r,c))

def bfs():
    temp = copy.deepcopy(grid)
    q = deque()
    
    for r in range(N):
        for c in range(M):
            if temp[r][c] == 2:
                q.append((r,c))
    
    while q:
        current_r, current_c = q.popleft()
        
        for dr, dc in direction:
            next_r = current_r + dr
            next_c = current_c + dc
            
            if 0 <= next_r < N and 0 <= next_c < M and temp[next_r][next_c] == 0:
                temp[next_r][next_c] = 2
                q.append((next_r, next_c))
    
    safe = 0
    for r in range(N):
        for c in range(M):
            if temp[r][c]==0:
                safe+=1

    return safe

get_wall_combi()

for walls in combinations(empty,3):

    for r,c in walls:
        grid[r][c] = 1

    answer = max(answer, bfs())

    for r,c in walls:
        grid[r][c] = 0

print(answer)

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i,j)
            elif maps[i][j] == 'E':
                end = (i,j)
            elif maps[i][j] == 'L':
                lever = (i,j)
    
    def bfs(s, e):
        visited = [[-1] * m for _ in range(n)]
        q = deque()
        direction = [[0,1], [1,0], [0,-1], [-1,0]]
        
        q.append(s)
        visited[s[0]][s[1]] = 0
        
        while q:
            x, y = q.popleft()
            
            if (x,y) == e:
                return visited[x][y]
            
            for i,j in direction:
                next_x = x + i
                next_y = y + j
            
                if 0 <= next_x < n and 0 <= next_y < m and maps[next_x][next_y] != 'X':
                    if visited[next_x][next_y] == -1:
                        visited[next_x][next_y] = visited[x][y] + 1
                        q.append((next_x, next_y))
                    
        return -1
    
    f = bfs(start, lever)
    
    if f == -1:
        return -1
    
    s = bfs(lever, end)
    
    if s == -1:
        return -1
    
    return f+s
N = int(input())

board = []

for i in range(N):
    board.append(list(input()))

visited = [[False] * N for _ in range(N)]
direction = [[-1,0], [0,1], [1,0], [0,-1]]
result = []

def dfs(x, y):
    global count
    
    for dx, dy in direction:
        next_x = x + dx
        next_y = y + dy
        
        if next_x >= 0 and next_y >= 0 and next_x < N and next_y < N:
            if not visited[next_x][next_y] and board[next_x][next_y] == "1":
                count += 1
                visited[next_x][next_y] = True
                dfs(next_x, next_y)

for i in range(N):
    for j in range(N):
        if not visited[i][j] and board[i][j] == "1":
            count = 1
            visited[i][j] = True
            dfs(i, j)
            result.append(count)

print(len(result))

result.sort()

for r in result:
    print(r)
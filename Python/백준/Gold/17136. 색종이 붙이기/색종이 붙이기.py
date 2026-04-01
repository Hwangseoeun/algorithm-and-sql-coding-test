from sys import stdin

board = []

for i in range(10):
    board.append(list(map(int, stdin.readline().split())))

paper = [5,5,5,5,5]
count = 100

def check(x, y, size):
    if x + size > 10 or y + size > 10:
        return False
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if board[i][j] != 1:
                return False
    
    return True

def fill(x, y, size, num):
    for i in range(x, x + size):
        for j in range(y, y + size):
            board[i][j] = num

def dfs(xy, cnt):
    global count
    
    if xy == 100:
        count = min(count, cnt)
        return
    
    x = xy // 10
    y = xy % 10
    
    if count <= cnt:
        return
    
    if board[x][y] == 1:
        for i in range(5, 0, -1):
            if paper[i-1] > 0 and check(x, y, i):
                paper[i-1] -= 1
                fill(x, y, i, 0)
                
                dfs(xy + 1, cnt + 1)
                
                paper[i-1] += 1
                fill(x, y, i, 1)
    
    else:
        dfs(xy + 1, cnt)

dfs(0, 0)

if count == 100:
    print(-1)
else:
    print(count)
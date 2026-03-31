N = int(input())

visited = [False] * N
visited_left = [False] * (2 * N - 1)
visited_right = [False] * (2 * N - 1)
count = 0

def dfs(depth):
    global count
    
    if depth == N:
        count += 1
        return
    
    for i in range(N):
        if not visited[i] and not visited_left[depth - i + N - 1] and not visited_right[depth + i]:
            visited[i] = True
            visited_left[depth - i + N - 1] = True
            visited_right[depth + i] = True
            
            dfs(depth + 1)
            
            visited[i] = False
            visited_left[depth - i + N - 1] = False
            visited_right[depth + i] = False

dfs(0)
print(count)
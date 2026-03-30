N, M = map(int, input().split())

def out(result):
    for r in result:
        print(r, end=" ")
    print()

def dfs(num, stack):
    global N, M
    
    visited[num-1] = True
    stack.append(num)
    
    if len(stack) == M:
        out(stack)
        stack.pop()
        visited[num-1] = False
        return
    
    for i in range(1, N+1):
        if not visited[i-1]:
            dfs(i, stack)
    
    stack.pop()
    visited[num-1] = False

for i in range(1, N+1):
    stack = []
    visited = [False] * N
    dfs(i, stack)
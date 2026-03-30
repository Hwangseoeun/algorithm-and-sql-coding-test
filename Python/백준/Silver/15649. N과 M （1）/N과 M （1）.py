N, M = map(int, input().split())

visited = [False] * N
stack = []

def out(result):
    for r in result:
        print(r, end=" ")
    print()

def dfs():
    if len(stack) == M:
        out(stack)
        return
    
    for i in range(1, N + 1):
        if not visited[i - 1]:
            visited[i - 1] = True
            stack.append(i)
            
            dfs()
            
            stack.pop()
            visited[i - 1] = False

dfs()
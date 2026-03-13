N, M = map(int, input().split())

friend = [[] for _ in range(N)]
visited = [False] * N
arrive = False

for _ in range(M):
    node1, node2 = map(int, input().split())
    
    friend[node1].append(node2)
    friend[node2].append(node1)

def dfs(recent, depth):
    global arrive
    
    if depth == 5 or arrive:
        arrive = True
        return

    visited[recent] = True
    
    for f in friend[recent]:
        if not visited[f]:
            dfs(f, depth + 1)
    
    visited[recent] = False

for i in range(N):
    dfs(i, 1)
    
    if arrive:
        break

if arrive:
    print("1")
else:
    print("0")
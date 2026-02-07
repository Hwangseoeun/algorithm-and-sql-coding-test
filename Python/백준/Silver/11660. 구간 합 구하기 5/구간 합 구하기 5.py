from sys import stdin

N, M = map(int, stdin.readline().split())

num = [[0]*(N+1) for i in range(N+1)]
S = [[0]*(N+1) for i in range(N+1)]

for i in range(1, N+1):
    arr = list(map(int, stdin.readline().split()))
    
    for j in range(1, N+1):
        num[i][j] = arr[j-1]
    
    for j in range(1, N+1):
        S[i][j] = S[i][j-1] + S[i-1][j] - S[i-1][j-1] + num[i][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    result = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    print(result)
M, N = map(int, input().split())

decimal = [True] * (N + 1)
decimal[0] = False
decimal[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if decimal[i]: 
        for j in range(i * 2, N + 1, i):
            decimal[j] = False

for i in range(M, N + 1):
    if decimal[i]:
        print(i)
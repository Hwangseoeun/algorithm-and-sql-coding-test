N, M = map(int, input().split())

num = list(map(int, input().split()))

S = [0] * N

for x in range(N):
    if x == 0:
        S[x] = num[x]
    
    else:
        S[x] = S[x-1] + num[x]

for y in range(M):
    i, j = map(int, input().split())
    
    if i-1 == 0:
        print(S[j-1])
    
    else:
        print(S[j-1] - S[i-2])
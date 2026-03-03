N = int(input())
P = list(map(int, input().split()))

for i in range(1, len(P)):
        while i > 0 and P[i] < P[i-1]:
            P[i], P[i-1] = P[i-1], P[i]
            i -= 1

S = [0] * N

for i in range(N):
    if i == 0:
        S[0] = P[0]
    
    else:
        S[i] = S[i-1] + P[i]

print(sum(S))
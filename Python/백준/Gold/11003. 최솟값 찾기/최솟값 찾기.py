from collections import deque
from sys import stdin

N, L = map(int, input().split())
A = list(map(int, stdin.readline().split()))

dq = deque([])

for i in range(N):
    if dq and dq[0][0] <= i-L:
        dq.popleft()
    
    while len(dq) >= 1 and dq[-1][1] > A[i]:
        dq.pop()
    
    dq.append((i, A[i]))

    print(dq[0][1], end=" ")
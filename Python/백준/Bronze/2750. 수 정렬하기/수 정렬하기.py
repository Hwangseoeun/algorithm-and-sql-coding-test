N = int(input())

A = [0] * N

for i in range(N):
    A[i] = int(input())

for i in range(N-1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]

for i in range(N):
    print(A[i])
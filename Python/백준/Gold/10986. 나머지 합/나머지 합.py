from sys import stdin

N, M = map(int, stdin.readline().split())

A = list(map(int, stdin.readline().split()))
S = [0] * len(A)

for i in range(len(A)):
    if i == 0:
        S[i] = A[i]
    
    else:
        S[i] = S[i-1] + A[i]

check = [0] * len(S)

for i in range(len(S)):
    check[i] = S[i] % M

result = 0
count = {}

for i in check:
    try: count[i] += 1
    except: count[i] = 1

for num in count.values():
    result += num * (num - 1) // 2

for i in range(len(check)):
    if check[i] == 0:
        result += 1

print(result)
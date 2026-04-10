from sys import stdin

N, K = map(int, input().split())

coins = []

for i in range(N):
    coins.append(int(stdin.readline()))

count = 0

for i in range(N-1, -1, -1):
    if coins[i] <= K:
        count += K // coins[i]
        K %= coins[i]

print(count)
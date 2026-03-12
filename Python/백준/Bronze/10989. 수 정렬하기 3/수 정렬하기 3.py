from sys import stdin

N = int(input())
count = [0] * 10001

for _ in range(N):
    count[int(stdin.readline())] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)
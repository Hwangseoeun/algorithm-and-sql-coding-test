from sys import stdin

N = int(input())

time = []

for i in range(N):
    s, e = map(int, stdin.readline().split())
    time.append((s,e))

time.sort(key = lambda t: (t[1], t[0]))

end = 0
count = 0

for s, e in time:
    if s >= end:
        end = e
        count += 1

print(count)
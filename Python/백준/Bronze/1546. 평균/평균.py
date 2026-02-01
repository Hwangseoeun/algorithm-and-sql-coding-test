N = int(input())
score = list(map(int, input().split(" ")))

top = max(score)

for i in range(N):
    score[i] = score[i] / top * 100

total = 0
for i in score:
    total += i

print(total/N)
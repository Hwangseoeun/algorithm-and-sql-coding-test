from collections import deque

N = int(input())
card = deque()

for i in range(N, 0, -1):
    card.append(i)

while len(card) > 1:
    card.pop()
    top = card.pop()
    card.appendleft(top)

print(card.pop())
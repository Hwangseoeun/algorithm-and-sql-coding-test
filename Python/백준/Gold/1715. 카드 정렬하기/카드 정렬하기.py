from sys import stdin
import heapq

N = int(input())

cards = []

for i in range(N):
    cards.append(int(stdin.readline()))

heapq.heapify(cards)

sum = 0

while cards:
    if len(cards) == 1:
        print(sum)
        break
    
    temp = heapq.heappop(cards) + heapq.heappop(cards)
    sum += temp
    
    heapq.heappush(cards, temp)
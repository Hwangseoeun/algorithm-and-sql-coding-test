from queue import PriorityQueue
from sys import stdin

N = int(input())
arr = PriorityQueue()

for i in range(N):
    num = int(stdin.readline())
    
    if num != 0:
        arr.put((abs(num), num))
    
    elif num == 0 and arr.qsize() == 0:
        print(0)
    
    else:
        min = arr.get()[1]
        print(min)

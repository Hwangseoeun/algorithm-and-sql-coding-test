import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = []
    
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    q = deque(days)
    count = 0
    
    while q:
        day = q.popleft()
        count = 1
        
        while q and q[0] <= day:
            q.popleft()
            count += 1
    
        answer.append(count)
    
    return answer
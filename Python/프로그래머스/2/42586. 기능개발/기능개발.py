import math

def solution(progresses, speeds):
    answer = []
    day = []
    
    for i in range(len(progresses)):
        day.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    temp_day = day[0]
    count = 0
    
    for d in day:
        if d <= temp_day:
            count += 1
        
        else:
            answer.append(count)
            temp_day = d
            count = 1
    
    answer.append(count)
    
    return answer
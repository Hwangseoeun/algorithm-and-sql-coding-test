def solution(progresses, speeds):
    answer = []
    
    days = [0] * len(progresses)
    
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            days[i] = (100 - progresses[i]) // speeds[i]
        else:
            days[i] = (100 - progresses[i]) // speeds[i] + 1
    
    current = days[0]
    count = 1

    for i in range(1, len(days)):
        if days[i] <= current:
            count += 1
        else:
            answer.append(count)
            current = days[i]
            count = 1

    answer.append(count)

    return answer
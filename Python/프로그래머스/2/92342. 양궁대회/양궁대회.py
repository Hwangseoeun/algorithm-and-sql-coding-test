def solution(n, info):
    answer = [-1]
    max_dif = 0
    
    def back(idx, cnt, ryan):
        nonlocal answer, max_dif
        
        if idx == 11 or cnt == 0:
            temp = ryan[:]
            
            if cnt > 0:
                temp[10] += cnt
            
            dif = 0
            
            for i in range(11):
                if temp[i] == 0 and info[i] == 0:
                    continue
                elif temp[i] > info[i]:
                    dif += (10-i)
                else:
                    dif -= (10-i)
            
            if dif > 0:
                if dif > max_dif:
                    answer = temp[:]
                    max_dif = dif
                elif dif == max_dif:
                    if answer[::-1] < temp[::-1]:
                        answer = temp[:]
            return
            
        elif info[idx] < cnt:
            ryan[idx] = info[idx] + 1
            back(idx+1, cnt-(info[idx] + 1), ryan)
            ryan[idx] = 0
        
        back(idx+1, cnt, ryan)
        
    back(0, n, [0] * 11)
    
    return answer
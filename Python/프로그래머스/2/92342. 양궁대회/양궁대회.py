def solution(n, info):
    max_dif = 0
    answer = [-1]
    
    def back(idx, cnt, ryan):
        nonlocal max_dif, answer
        
        if idx == 11 or cnt == 0:
            temp = ryan[:]
            
            if cnt > 0:
                temp[10] += cnt
            
            a_score, r_score = 0, 0
            
            for i in range(11):
                if info[i] == 0 and temp[i] == 0:
                    continue
                
                if info[i] < temp[i]:
                    r_score += (10-i)
                
                else:
                    a_score += (10-i)
            
            dif = r_score - a_score
            
            if dif > 0:
                if dif > max_dif:
                    max_dif = dif
                    answer = temp[:]
                    
                elif dif == max_dif:
                    if answer[::-1] < temp[::-1]:
                        answer = temp[:]
            return

        if cnt >= info[idx] + 1:
            ryan[idx] = info[idx] + 1
            back(idx + 1, cnt - (info[idx] + 1), ryan)
            ryan[idx] = 0
        
        back(idx+1, cnt, ryan)
        
    back(0, n, [0]*11)
    
    return answer
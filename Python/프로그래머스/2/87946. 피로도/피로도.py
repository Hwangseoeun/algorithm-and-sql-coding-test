def solution(k, dungeons):
    max_cnt = 0
    visited = [False] * len(dungeons)
    
    def back(p, cnt):
        nonlocal max_cnt, visited
        
        if cnt > max_cnt:
            max_cnt = cnt
        
        for i in range(len(dungeons)):
            if not visited[i] and p >= dungeons[i][0]:
                visited[i] = True
                back(p-dungeons[i][1], cnt+1)
                visited[i] = False
                
    back(k, 0)
    
    return max_cnt
def solution(k, dungeons):
    maxCount = 0;
    visited = [False for _ in range(len(dungeons))]
    
    def dfs(k, count):
        nonlocal maxCount
    
        maxCount = max(maxCount, count)
    
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k - dungeons[i][1], count + 1)
                visited[i] = False
    
    dfs(k, 0)
    
    return maxCount
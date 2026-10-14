from itertools import combinations

def solution(relation):
    def checkUnique(relation, com):
        words = []
        
        for i in range(len(relation)):
            word = "s"
            for c in com:
                word += relation[i][c]
            
            words.append(word)
        
        if len(set(words)) == len(relation):
            return True
        
        return False
        
    
    idx = [i for i in range(len(relation[0]))]
    combi = []
    result = []
    
    for i in range(1, len(relation[0])+1):
        for c in combinations(idx, i):
            combi.append(c)
    
    for i in combi:
        isMinimal = True
        for r in result:
            if set(r).issubset(set(i)):
                isMinimal = False
                break
        
        if not isMinimal:
            continue
    
        if checkUnique(relation, i):
            result.append(i)        
    
    return len(result)
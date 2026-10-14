def solution(s):
    arr = []
    
    for i in list(s):
        if i == '(':
            arr.append(i)
        
        elif i == ')':
            if not arr:
                return False
            else:
                arr.pop()
    
    if arr:
        return False

    return True
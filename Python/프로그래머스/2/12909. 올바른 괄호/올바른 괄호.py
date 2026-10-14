def solution(s):
    arr = []
    
    for i in s:
        if i == '(':
            arr.append(i)
        
        elif i == ')':
            if not arr:
                return False
            else:
                arr.pop()

    return not arr
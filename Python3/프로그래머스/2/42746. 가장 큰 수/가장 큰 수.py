from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a: return -1
    if a + b < b + a: return 1
    return 0

def solution(numbers):
    numbers = [str(n) for n in numbers]
    
    numbers = sorted(numbers, key=cmp_to_key(compare))
    
    if numbers[0] == "0":
        return "0"
    
    return "".join(numbers)
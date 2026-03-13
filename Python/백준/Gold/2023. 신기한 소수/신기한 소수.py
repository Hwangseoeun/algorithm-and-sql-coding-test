N = int(input())

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def dfs(number, digit):
    if digit == N:
        if isPrime(number):
            print(number)
    
    for i in range(1, 10):
        if i % 2 == 0:
            continue
        
        if isPrime(number * 10 + i):
            dfs(number * 10 + i, digit + 1)

dfs(2, 1)
dfs(3, 1)
dfs(5, 1)
dfs(7, 1)
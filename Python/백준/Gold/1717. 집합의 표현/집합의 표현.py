from sys import stdin

N, M = map(int, input().split())

nums = [i for i in range(N+1)]

def find(num):
    if nums[num] == num:
        return num
    
    nums[num] = find(nums[num])
    return find(nums[num])

def union(n1, n2):
    a = find(n1)
    b = find(n2)
    
    nums[b] = a

for i in range(M):
    option, num1, num2 = map(int, stdin.readline().split())
    
    if option == 0:
        union(num1, num2)
    
    elif option == 1:
        if find(num1) == find(num2):
            print("YES")
        else:
            print("NO")
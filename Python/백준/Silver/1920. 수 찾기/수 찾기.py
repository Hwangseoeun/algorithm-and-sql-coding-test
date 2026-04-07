import sys
import copy

sys.setrecursionlimit(10 ** 6)

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(input())
X = list(map(int, sys.stdin.readline().split()))

result = []

def find(start, finish, num):
    global arr
    
    if start > finish:
        result.append(0)
        return
    
    mid = (start + finish) // 2
    
    if A[mid] == num:
        result.append(1)
        return
    
    elif A[mid] > num:
        find(start, mid-1, num)
    
    else:
        find(mid+1, finish, num)

for num in X:
    find(0, N-1, num)

for r in result:
    print(r)
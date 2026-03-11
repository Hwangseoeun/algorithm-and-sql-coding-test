from sys import stdin

N = int(input())
A = list(map(int, stdin.readline().split()))

count = 0

def sort(start, end):    
    global count
    
    if end - start < 1:
        return
    
    middle = start + (end - start) // 2
    
    sort(start, middle)
    sort(middle + 1, end)
    
    temp = []
    idx1 = start
    idx2 = middle + 1
    
    while idx1 <= middle and idx2 <= end:
        if A[idx1] <= A[idx2]:
            temp.append(A[idx1])
            idx1 += 1
        else:
            temp.append(A[idx2])
            count += (middle - idx1 + 1)
            idx2 += 1
    
    while idx1 <= middle:
        temp.append(A[idx1])
        idx1 += 1
    
    while idx2 <= end:
        temp.append(A[idx2])
        idx2 += 1
    
    for i in range(len(temp)):        
        A[start + i] = temp[i]

sort(0, N-1)

print(count)
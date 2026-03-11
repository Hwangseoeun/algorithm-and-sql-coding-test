from sys import stdin

N = int(input())
nums = []

for i in range(N):
    nums.append(int(stdin.readline()))

def sort(start, end):    
    if end - start < 1:
        return

    middle = start + (end - start) // 2
    
    sort(start, middle)
    sort(middle + 1, end)
    
    temp = []
    idx1 = start
    idx2 = middle + 1
    
    while idx1 <= middle and idx2 <= end:
        if nums[idx1] < nums[idx2]:
            temp.append(nums[idx1])
            idx1 += 1
        else:
            temp.append(nums[idx2])
            idx2 += 1
    
    while idx1 <= middle:
        temp.append(nums[idx1])
        idx1 += 1

    while idx2 <= end:
        temp.append(nums[idx2])
        idx2 += 1
    
    for i in range(len(temp)):
        nums[start + i] = temp[i]

sort(0,N-1)

for i in range(N):
    print(nums[i])
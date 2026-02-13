from sys import stdin

N = int(input())
nums = list(map(int, stdin.readline().split()))
nums.sort()

count = 0

for i in range(N):
    startIdx = 0
    endIdx = N-1
    
    while startIdx < endIdx:
        if nums[startIdx] + nums[endIdx] == nums[i]:
            if startIdx != i and endIdx != i:
                count += 1
                break
            elif startIdx == i:
                startIdx += 1
            elif endIdx == i:
                endIdx -= 1
            
        elif nums[startIdx] + nums[endIdx] > nums[i]:
            endIdx -= 1
        elif nums[startIdx] + nums[endIdx] < nums[i]:
            startIdx += 1

print(count)
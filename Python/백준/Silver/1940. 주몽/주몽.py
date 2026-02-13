from sys import stdin

N = int(input())
M = int(input())

nums = list(map(int, stdin.readline().split()))
nums.sort()

count = 0
startIdx = 0
endIdx = N-1

while startIdx < endIdx:
    if nums[startIdx] + nums[endIdx] == M:
        count += 1
        startIdx += 1
        endIdx -= 1
    elif nums[startIdx] + nums[endIdx] > M:
        endIdx -= 1
    elif nums[startIdx] + nums[endIdx] < M:
        startIdx += 1

print(count)
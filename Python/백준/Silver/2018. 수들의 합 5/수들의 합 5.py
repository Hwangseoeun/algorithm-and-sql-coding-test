N = int(input())

sum = 1
count = 1
startIdx = 1
endIdx = 1

while endIdx != N:
    if sum == N:
        endIdx += 1
        sum += endIdx
        count += 1
    elif sum > N:
        sum -= startIdx
        startIdx += 1
    elif sum < N:
        endIdx += 1
        sum += endIdx

print(count)
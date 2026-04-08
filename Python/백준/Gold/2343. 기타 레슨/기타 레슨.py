from sys import stdin

N, M = map(int, input().split())
vidio_time = list(map(int, stdin.readline().split()))

def find_count(start, end):
    count = 1
    current_sum = 0
    mid = (start + end) // 2
    
    for time in vidio_time:
        if current_sum + time > mid: 
            count += 1
            current_sum = time
        else:
            current_sum += time
    
    return count

start = max(vidio_time)
end = sum(vidio_time)
result = 0

while start <= end:
    count = find_count(start, end)
    mid = (start + end) // 2
    
    if count <= M:
        end = mid - 1
        result = mid
    
    elif count > M:
        start = mid + 1

print(result)
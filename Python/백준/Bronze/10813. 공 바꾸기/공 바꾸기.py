N, M = map(int, input().split(" "))

arr = list(range(1, N+1))

for x in range(M):
    i, j = map(int, input().split(" "))
    
    temp = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = temp
    
for y in arr:
    print(y, end=" ")
    
print()

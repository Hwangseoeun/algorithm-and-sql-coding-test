N, M = map(int, input().split(" "))

arr = list(range(1, N+1))

for x in range(M):
    i, j = map(int, input().split(" "))
    
    for y in range(1, j+1):
        if y > (j-i)//2+1:
            break
        
        temp = arr[i+y-2]
        arr[i+y-2] = arr[j-y]
        arr[j-y] = temp
        
for z in arr:
    print(z, end=" ")
    
print()
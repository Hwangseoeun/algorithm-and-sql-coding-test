right = [1,1,2,2,2,8]

find = list(map(int, input().split(" ")))

for i in range(len(right)):
    num = right[i] - find[i]
    print(num, end=" ")

print()
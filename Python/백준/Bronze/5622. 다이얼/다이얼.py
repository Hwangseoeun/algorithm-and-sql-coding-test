arr = list(input())

dial = {
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "Q", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y", "Z"]
    }

num = [0] * len(arr)

for i in range(len(arr)):
    for j, k in dial.items():
        if arr[i] in k:
            num[i] = int(j)
            break

total = 0

for i in num:
    total += 2
    for j in range(i-1):
        total += 1

print(total)
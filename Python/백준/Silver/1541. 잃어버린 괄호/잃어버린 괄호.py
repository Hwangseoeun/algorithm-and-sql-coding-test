bundle = input().split("-")

result = 0

for i in range(len(bundle)):
    nums = bundle[i].split("+")
    
    temp = 0
    
    for n in nums:
        temp += int(n)
    
    if i == 0:
        result += temp
    
    else:
        result -= temp

print(result)
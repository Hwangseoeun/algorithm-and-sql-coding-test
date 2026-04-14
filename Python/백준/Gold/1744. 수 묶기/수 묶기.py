N = int(input())

positive = []
negative = []
zero_cnt = 0
one_cnt = 0

for i in range(N):
    num = int(input())
    
    if num == 0:
        zero_cnt += 1
    
    elif num == 1:
        one_cnt += 1
    
    elif num > 0 :
        positive.append(num)
    
    elif num < 0 :
        negative.append(num)

sum = 0

positive.sort()

for i in range(len(positive)-1, -1, -2):
    if len(positive) % 2 != 0 and i == 0:
        sum += positive[i]
    
    else:
        sum += positive[i] * positive[i-1]

negative.sort()

for i in range(0, len(negative), 2):
    if len(negative) % 2 != 0 and i == len(negative) - 1:
        if zero_cnt > 0:
            sum += negative[i] * 0
            zero_cnt -= 1
        
        else:
            sum += negative[i]
    
    else:
        sum += negative[i] * negative[i+1]

sum += one_cnt

print(sum)
import copy

N = int(input())

count = 0

for i in range(N):
    word = list(input())
    stack = []
    wordNum = len(list(set(word)))
    
    for j in range(len(word)):
        if len(stack) == 0 or word[j] != stack[-1]:
            stack.append(word[j])
        elif word[j] == stack[-1]:
            continue
    
    if len(stack) == wordNum:
        count += 1

print(count)
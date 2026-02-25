N = int(input())
A = list(map(int, input().split()))

idxStack = []
stack = [0] * N

for i in range(len(A)):
    while len(idxStack) != 0 and A[idxStack[-1]] < A[i]:
        top = idxStack[-1]
        
        stack[top] = A[i]
        idxStack.pop()
    
    idxStack.append(i)
    
while len(idxStack) != 0:
    idx = idxStack.pop()
    stack[idx] = -1

for i in range(len(A)):
    print(stack[i], end=" ")
print()
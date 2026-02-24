def isOK():
    stack = []
    num = 1
    for i in range(n):
        while data[i] >= num:
            stack.append(num)
            num += 1
            out.append('+')
        if len(stack) > 0 and data[i] == stack[-1]:
            stack.pop()
            out.append('-')
        else:
            return False
    return True


# main program
n = int(input())
data = []  # 입력 데이터
for i in range(n):
    data.append(int(input()))
out = []  # 출력 데이터

if isOK():
    for x in out:
        print(x)
else:
    print('NO')
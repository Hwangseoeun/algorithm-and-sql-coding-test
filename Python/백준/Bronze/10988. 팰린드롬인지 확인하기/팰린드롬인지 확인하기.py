word = list(input())

for i in range(len(word)):
    if word[i] != word[len(word)-1-i]:
        print(0)
        break
    
    if i == len(word)-1:
        if word[i] != word[len(word)-1-i]:
            print(0)
        else:
            print(1)
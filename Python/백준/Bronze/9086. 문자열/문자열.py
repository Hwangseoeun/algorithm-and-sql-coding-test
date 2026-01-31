T = int(input())

for i in range (T):
    word = list(input())
    print("{0}{1}".format(word[0], word[len(word)-1]))
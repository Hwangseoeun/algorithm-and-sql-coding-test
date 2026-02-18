word = list(input().strip())

count = 0
idx = 0

while idx < len(word):
    if word[idx] == "c":
        if idx != len(word)-1 and word[idx+1] == "=":
            count += 1
            idx += 2
            continue
        elif idx != len(word)-1 and word[idx+1] == "-":
            count += 1
            idx += 2
            continue
        else:
            count += 1
            idx += 1
            continue
    
    elif word[idx] == "d":
        if idx != len(word)-1 and word[idx+1] == "z":
            if idx != len(word)-2 and word[idx+2] == "=":
                count += 1
                idx += 3
                continue
            else:
                count += 1
                idx += 1
                continue
        elif idx != len(word)-1 and word[idx+1] == "-":
            count += 1
            idx += 2
            continue
        else:
            count += 1
            idx += 1
            continue
    
    elif word[idx] == "l":
        if idx != len(word)-1 and word[idx+1] == "j":
            count += 1
            idx += 2
            continue
        else:
            count += 1
            idx += 1
            continue
    
    elif word[idx] == "n":
        if idx != len(word)-1 and word[idx+1] == "j":
            count += 1
            idx += 2
            continue
        else:
            count += 1
            idx += 1
            continue
    
    elif word[idx] == "s":
        if idx != len(word)-1 and word[idx+1] == "=":
            count += 1
            idx += 2
            continue
        else:
            count += 1
            idx += 1
            continue
    
    elif word[idx] == "z":
        if idx != len(word)-1 and word[idx+1] == "=":
            count += 1
            idx += 2
            continue
        else:
            count += 1
            idx += 1
            continue
    
    else:
        count += 1
        idx += 1
        continue

print(count)
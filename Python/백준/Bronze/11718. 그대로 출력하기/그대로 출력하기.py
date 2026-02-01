sentence = []

while True:
    try:
        input_data = input()
    
        if len(sentence) > 100:
            break
    
        sentence.append(input_data)
        
    except EOFError:
        break
    
for i in sentence:
    print(i)
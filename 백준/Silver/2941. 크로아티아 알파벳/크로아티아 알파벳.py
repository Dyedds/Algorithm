#2941번 크로아티아 알파벳
word = input()
count = 0
for i in range(len(word)):
    if(word[i] == '='):
        count = count -1
    elif(word[i] == '-'):
        count = count -1
    elif(word[i] == 'd'):
        if(i != (len(word)-1)):
            if(word[i+1] == 'z'):
                if(i != (len(word)-2)):
                    if(word[i+2] == '='):
                        count = count - 1
    elif(word[i] == 'l'):
        if(i != (len(word)-1)):
            if(word[i+1] == 'j'):
                count = count - 1
    elif(word[i] == 'n'):
        if(i != (len(word)-1)):
            if(word[i+1] == 'j'):
                count = count - 1
    count = count + 1
print(count)

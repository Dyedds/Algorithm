while(True):
    count = 0
    string = input()
    if(string == '#'):
        break
    string_list = list(map(str, str(string)))
    for i in range(len(string_list)):
        if (string_list[i] == 'a'):
            count = count + 1
        elif (string_list[i] == 'e'):
            count = count + 1
        elif (string_list[i] == 'i'):
            count = count + 1
        elif (string_list[i] == 'o'):
            count = count + 1
        elif (string_list[i] == 'u'):
            count = count + 1
        elif (string_list[i] == 'A'):
            count = count + 1
        elif (string_list[i] == 'E'):
            count = count + 1
        elif (string_list[i] == 'I'):
            count = count + 1
        elif (string_list[i] == 'O'):
            count = count + 1
        elif (string_list[i] == 'U'):
            count = count + 1 
    print(count)

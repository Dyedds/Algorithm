def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if(myString[i] == 'a'):
            answer = answer + 'A'
        elif(myString[i] == 'A'):
            answer = answer + 'A'
        else:
            answer = answer + myString[i].lower()
    return answer
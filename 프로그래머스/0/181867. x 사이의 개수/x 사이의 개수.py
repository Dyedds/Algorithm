def solution(myString):
    answer = []
    count = 0
    for i in myString:
        if(i=='x'):
            answer.append(count)
            count = 0
        else:
            count = count + 1
    answer.append(count)
    return answer
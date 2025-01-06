def solution(myString, pat):
    answer = 0
    compare = ''
    for i in myString:
        if(i == "A"):
            compare = compare + 'B'
        else:
            compare = compare + 'A'
    if(pat in compare):
        answer = 1
    else:
        answer = 0
    return answer
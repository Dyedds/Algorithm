def solution(rny_string):
    answer = ''
    for i in rny_string:
        if(i=='m'):
            answer = answer + 'rn'
        else:
            answer = answer + i
    return answer
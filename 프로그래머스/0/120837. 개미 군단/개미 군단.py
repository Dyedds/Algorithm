def solution(hp):
    answer = 0
    while(hp > 0):
        if(hp >= 5):
            answer = answer + 1
            hp = hp - 5
        elif(hp >= 3):
            answer = answer + 1
            hp = hp - 3
        else:
            answer = answer + 1
            hp = hp - 1
    return answer
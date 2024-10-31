def solution(common):
    answer = 0
    # 등차수열인 경우
    if(common[1] - common[0] == common[2] - common[1]):
        answer = common[-1] + common[1] - common[0]
    # 등비수열인 경우
    else:
        answer = common[-1] * common[1] / common[0]
    return answer
def solution(num_list):
    a = 0
    b = 0
    for i in num_list:
        if i % 2 == 0:
            b = b * 10 + i
        else:
            a = a * 10 + i
    
    answer = a + b
    return answer

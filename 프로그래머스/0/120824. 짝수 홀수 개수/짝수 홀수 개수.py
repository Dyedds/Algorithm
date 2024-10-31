def solution(num_list):
    answer = []
    even = 0
    odd = 0
    for i in num_list:
        if(i % 2 == 0):
            even = even + 1
        else:
            odd = odd + 1
    answer.append(even)
    answer.append(odd)
    return answer
def solution(num, k):

    num = str(num)
    k = str(k)

    for i in range(len(num)):
        if num[i] == k:
            return i + 1
    
    return -1

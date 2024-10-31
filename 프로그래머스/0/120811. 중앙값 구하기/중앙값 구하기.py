def solution(array):
    answer = 0
    array.sort()
    answer = len(array) // 2
    return array[answer]
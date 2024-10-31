import math

def solution(num1, num2):
    answer = 0
    answer = num1 / num2 * 1000
    return math.trunc(answer)
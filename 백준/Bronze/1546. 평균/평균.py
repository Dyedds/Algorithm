#1546번 평균

import sys
import math

N = int(input())
score_list = []

score_list = list(map(int,input().split()))

M = max(score_list)
new_score_list = []
sum = 0

for i in range(N):
    new_score_list.append((score_list[i]/M) * 100)
    sum = sum + new_score_list[i]

print(sum/N)
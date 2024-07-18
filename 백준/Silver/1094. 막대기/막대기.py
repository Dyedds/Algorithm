# 1094번 막대기

sum = int(input())
stick = [64,32,16,8,4,2,1]
count = 0

for i in stick:
    if(i <= sum):
        sum = sum - i
        count = count + 1

print (count)

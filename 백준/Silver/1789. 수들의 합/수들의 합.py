S = int(input())
sum = 0
num = 1
count = 0
while(1):
    sum = sum + num
    count = count + 1
    if(sum > S):
        count = count - 1
        break
    num = num + 1
print(count)
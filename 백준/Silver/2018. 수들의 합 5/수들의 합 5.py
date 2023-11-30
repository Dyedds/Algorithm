#2018번 수들의 합5
target_num = int(input())

start,end,counter,sum = 1,1,1,1

while end < target_num:
    if(sum < target_num):       #sum값이 더 작을 때
        end = end + 1
        sum = sum + end
    elif(sum == target_num):
        counter = counter + 1   #sum값이 같을 때
        end = end + 1
        sum = sum + end
    else:                       #sum값이 더 클 때
        sum = sum - start       #sum값에서 start값을 빼주면 바로 다음 경우의 합을 한번에 구할 수 있음
        start = start + 1
print(counter)


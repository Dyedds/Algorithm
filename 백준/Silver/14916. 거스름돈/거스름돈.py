#14916번 거스름돈

n = int(input())
count = 0

while(True):
    if(n % 5 == 0):             #5의 배수이면 
        count = count + n//5    #5로만 나눈 것이 정답
        break
    else:
        n = n - 2               #5의 배수가 아니면 2(2원)씩 빼면서 5의 배수로 만듦
        count = count + 1

if(n < 0):                      #음수가 되면
    print(-1)                   #거슬러 줄 수 없음
else:
    print(count)                #while문을 빠져나와 음수가 아니면 count개수 출

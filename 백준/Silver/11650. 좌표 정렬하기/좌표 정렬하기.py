#11650번 좌표 정렬하기

N = int(input())

list = []
for i in range(N):
    [x, y] = map(int,input().split())
    list.append([x,y])

answer_list = sorted(list)

for i in range(N):
    print(answer_list[i][0], answer_list[i][1])

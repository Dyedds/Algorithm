#2740번 행렬 곱셈
N,M = map(int,input().split())
listA = []
listB = []
answerlist=[]
for i in range(N):
    listA.append(list(map(int,input().split())))
A,B = map(int,input().split())
for i in range(A):
    listB.append(list(map(int,input().split())))

for i in range(N):
    answerlist.append([0] * B)

for i in range(N):
    for j in range(B):
        sum = 0
        for k in range(A):
            sum = sum + listA[i][k]*listB[k][j]
        answerlist[i][j] = sum

for i in answerlist:
    print(' '.join(map(str, i)))

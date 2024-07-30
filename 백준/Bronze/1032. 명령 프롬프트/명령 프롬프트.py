#1032번

N = int(input())
list = []
ans = []
if N == 1:
    print(input())
    exit()
for i in range(N):
    element = input()
    list.append(element)
ans = ['']*len(list[0])
for i in range(1,N):
    for j in range(len(list[0])):
        if((list[i][j] == list[i-1][j]) and (ans[j] != '?')):
            ans[j] = list[i][j]
        else:
            ans[j] = '?'
print(''.join(ans))
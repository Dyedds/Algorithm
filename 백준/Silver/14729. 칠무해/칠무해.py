#14729번 칠무해

N = int(input())
score_list = []

for i in range(N):
    score = float(input())
    score_list.append(score)

score_list.sort()
for i in range(7):
    print("{:.3f}".format(score_list[i]))

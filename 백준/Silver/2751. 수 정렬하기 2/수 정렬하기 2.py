n = int(input())
answer_list = []
for i in range(n):
    num = int(input())
    answer_list.append(num)
l = sorted(answer_list, reverse = True)

for i in reversed(range(n)):
    print(l[i])

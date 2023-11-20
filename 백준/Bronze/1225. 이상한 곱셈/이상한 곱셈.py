A, B = map(int,(input().split()))
A_list = list(map(int, str(A)))
B_list = list(map(int, str(B)))

sum = 0
for i in range(len(A_list)):
    for j in range(len(B_list)):
        sum = sum + A_list[i] * B_list[j]
print(sum)

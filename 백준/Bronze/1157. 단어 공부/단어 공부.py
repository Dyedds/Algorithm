# 1157번

N = input().upper()
N_list = list(set(N))

N_count = []
for i in N_list:
    N_count.append(N.count(i))
if N_count.count(max(N_count)) > 1:
    print("?")
else:
    print(N_list[N_count.index(max(N_count))])

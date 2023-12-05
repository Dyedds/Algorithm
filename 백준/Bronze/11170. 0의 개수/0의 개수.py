#11170번 0의 개수
T = int(input())

for i in range(T):
    count = 0
    N,M = map(int,input().split())
    for j in range(N,M+1):
        N_list = list(map(int,str(j)))
        for k in N_list:
            if(k == 0):
                count = count + 1
    print(count)

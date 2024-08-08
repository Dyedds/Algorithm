N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
start = 0
current_sum = 0

for end in range(N):
    current_sum += A[end]

    while current_sum >= M:
        if current_sum == M:
            cnt += 1
        current_sum -= A[start]
        start += 1

print(cnt)

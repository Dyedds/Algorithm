# 4299

sum, dif = map(int, input().split())

if(sum < 0 or sum-dif < 0 or (sum+dif)%2):
    print(-1)
else:
    print((sum + dif) // 2, (sum - dif) // 2)
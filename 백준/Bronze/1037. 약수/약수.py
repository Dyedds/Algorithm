count_divisor = int(input())
divisor = list(map(int,input().split()))
result = min(divisor) * max(divisor)
print(result)
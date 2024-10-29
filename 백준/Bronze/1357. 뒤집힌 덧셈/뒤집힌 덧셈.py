#1357

X, Y = map(int, input().split())
result = int(str(X)[::-1]) + int(str(Y)[::-1])
print(int(str(result)[::-1]))
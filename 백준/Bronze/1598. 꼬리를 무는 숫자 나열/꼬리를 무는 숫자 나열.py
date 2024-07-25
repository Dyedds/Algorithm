#1598번

X, Y = map(int, input().split())

X = X - 1
Y = Y - 1
print(abs(X//4 - Y//4) + abs(X%4-Y%4))
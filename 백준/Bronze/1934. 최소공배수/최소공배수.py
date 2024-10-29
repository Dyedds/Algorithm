#1934

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    A, B = a,b

    while a % b != 0:
        a, b = b, a % b
    print(A * B // b)
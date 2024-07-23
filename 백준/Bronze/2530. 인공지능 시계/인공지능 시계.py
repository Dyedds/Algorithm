A, B, C = map(int, input().split())
D = int(input())

x = D // 60
y = D % 60
B = B + x
C = C + y
while True:
    if C >= 60:
        C = C - 60
        B = B + 1
    else:
        if B >= 60:
            B = B - 60
            A = A + 1
        else:
                if A >= 24:
                    A = A - 24
                else:
                    break

print(A, B, C)
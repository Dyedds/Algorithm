import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    a, b = map(int,(input().split()))
    remain = (a % 10)
    if (remain == 0):
        print(10)
    elif (remain == 1) or (remain == 5) or (remain == 6):
        print(remain)
    elif (remain == 4) or (remain == 9):
        if((b % 2) == 0):
            print((remain * remain) % 10)
        else:
            print(remain % 10)
    else:
        bb = b% 4
        if(bb == 0):
            print((remain ** 4) %10)
        else:
            print((remain ** bb)%10)
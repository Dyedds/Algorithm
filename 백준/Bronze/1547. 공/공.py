import sys

change_count = int(input())
C_1 = 1
C_2 = 0
C_3 = 0
for i in range(change_count):
    X, Y = map(int,(sys.stdin.readline().split()))
    su = X+Y
    if(su == 3):
        C_1,C_2 = C_2,C_1
    elif(su == 4):
        C_1,C_3 = C_3,C_1
    else:
        C_2,C_3 = C_3,C_2
if(C_1 == 1):
    print(1)
elif(C_2 == 1):
    print(2)
else:
    print(3)

#1075

N = int(input())
F = int(input())
num = N - N%100
while(True):
    remain = num%100
    if(num % F == 0):
        print(format(remain, '02'))
        break
    else:
        num = num + 1
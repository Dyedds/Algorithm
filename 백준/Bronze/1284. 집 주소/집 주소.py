import sys

while(True):
    num = int(sys.stdin.readline())
    if(num == 0):
        break
    else:
        sum = 2
        num_list = list(map(int, str(num)))
        for i in range(len(num_list)):
            if(num_list[i] == 1):
                sum = sum + 2
            elif(num_list[i] == 0):
                sum = sum + 4
            else:
                sum = sum + 3
            sum = sum + 1
        sum = sum - 1
        print(sum)
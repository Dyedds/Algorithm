#1343번 폴리오미노
import sys

answer_list = []
board = list(input())
count = 0
for i in range(len(board)):
    if(board[i] == 'X'):
        count = count + 1
    elif(board[i] == '.'):
        if(count == 2):
            answer_list.append("BB")
            answer_list.append(".")
        elif(count == 0):
            answer_list.append(".")
            continue
        else:
            print(-1)
            sys.exit()
    
        count = 0
    if(count == 4):
        answer_list.append("AAAA")
        count = 0

if(count == 2):
    answer_list.append("BB")
    count = 0

if(count == 0):
    print(''.join(answer_list))
else:
    print(-1)

#1924번 2007년
month, date = map(int,input().split())
month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
total_date = 0
for i in range(month - 1):
    total_date = total_date + month_list[i]
answer_day = (total_date + date) % 7

if(answer_day == 1):
    print('MON')
elif(answer_day == 2):
    print('TUE')
elif(answer_day == 3):
    print('WED')
elif(answer_day == 4):
    print('THU')
elif(answer_day == 5):
    print('FRI')
elif(answer_day == 6):
    print('SAT')
else:
    print('SUN')

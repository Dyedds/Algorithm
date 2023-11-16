count_call = int(input())
count_time = list(map(int,input().split()))
Yfee = 0
Mfee = 0

for i in range(count_call):
    Yfee = Yfee + 10 + (count_time[i]//30) * 10
for i in range(count_call):
    Mfee = Mfee + 15 + (count_time[i]//60) * 15

if(Yfee > Mfee):
    print('M', Mfee)
elif(Yfee < Mfee):
    print('Y', Yfee)
else:
    print('Y M', Mfee)
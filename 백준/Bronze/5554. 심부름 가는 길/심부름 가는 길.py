#5554번

school = int(input())
PC = int(input())
education = int(input())
home = int(input())

total = school + PC + education + home
x , y = 0,0
while(True):
    if total >= 60:
        total = total-60
        x = x + 1
    else:
        break
y = total
print(x)
print(y)
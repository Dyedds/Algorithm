#5585번 거스름돈

money = int(input())
money = 1000 - money
count = 0

while(money != 0):
    if(money >= 500):
        money = money - 500
        count = count + 1
    elif(money >= 100):
        money = money - 100
        count = count + 1
    elif(money >= 50):
        money = money - 50
        count = count + 1
    elif(money >= 10):
        money = money - 10
        count = count + 1
    elif(money >= 5):
        money  = money - 5
        count = count + 1
    else:
        money = money - 1
        count = count + 1
print(count)

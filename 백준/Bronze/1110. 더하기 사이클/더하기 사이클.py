num = int(input())

num_list = list(map(int, str(num)))
if(num < 10):
    num_list.insert(0, 0)

check_list = [] + num_list

count = 0

while(True):
    sum_num = check_list[0] + check_list[1]
    check_list[0] = check_list[1]
    check_list[1] = sum_num % 10
    
    count = count + 1
    if(check_list == num_list):
        print(count)
        break
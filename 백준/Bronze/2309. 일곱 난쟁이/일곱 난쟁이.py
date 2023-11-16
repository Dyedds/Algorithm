import sys

height_list = []
remove_list = []
su = 0
for i in range(9):
    height = input()
    height_list.append(int(height))
    su = su + height_list[i]

for i in range(len(height_list)):
    for j in range(i+1, len(height_list)):
        sum_tmp = su 
        seven_sum = sum_tmp - height_list[i] - height_list[j]
        if(seven_sum == 100):
            remove_list.append(height_list[i])
            remove_list.append(height_list[j])
            height_list.remove(remove_list[0])
            height_list.remove(remove_list[1])
            height_list.sort()
            for k in range(len(height_list)):
                print(height_list[k])
            exit()
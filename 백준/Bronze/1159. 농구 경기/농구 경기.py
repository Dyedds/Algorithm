#1159번 농구 경기

N = int(input())
list_name = []
result = []

for i in range(N):
    name = input()
    list_name.append(name[0])

first_name = set(list_name)

for i in first_name:
    if(list_name.count(i) >= 5):
       result.append(i)
if(len(result) > 0):
   print(''.join(sorted(result)))
else:
    print("PREDAJA")
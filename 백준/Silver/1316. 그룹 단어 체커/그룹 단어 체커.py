#1316번 그룹 단어 체커
N = int(input())

count = N
for i in range(N):
    string = input()
    for j in range(len(string)-1):
        if(string[j] == string[j+1]):
           pass
        elif string[j] in string[j+1:]:
             count = count - 1
             break

print(count)
str = input()
answer = ''
for i in str:
    if(i.isupper()):
        answer = answer + i.lower()
    else:
        answer = answer + i.upper()
print(answer)
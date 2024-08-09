#1259

pelinum = 0
while(True):
    pelinum = input()
    if pelinum == '0':
        break
    is_pelinum = True
    for i in range(len(pelinum)//2):
        if pelinum[i] != pelinum[len(pelinum)-i-1]:
            print("no")
            is_pelinum = False
            break
    if is_pelinum:
        print("yes")
#2526번 싸이클

N, P = map(int, input().split())
list1 = []
tmp = N
while True:
    store = (tmp * N) % P
    if store in list1:
        print(len(list1) - list1.index(store)) 
        break
    list1.append(store)
    tmp = store
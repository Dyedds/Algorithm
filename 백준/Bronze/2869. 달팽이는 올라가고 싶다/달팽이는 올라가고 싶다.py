A,B,V = map(int,input().split())
height = 0
day = 0

if (V-B) % (A-B) == 0:
    print((V-B)//(A-B))
else:
    print((V-B)//(A-B)+1)

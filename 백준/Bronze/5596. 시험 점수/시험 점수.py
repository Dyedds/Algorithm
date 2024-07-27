# 5596번

inf,math,sci,eng = map(int,input().split())
inf2,math2,sci2,eng2 = map(int,input().split())

if inf + math + sci + eng > inf2 + math2 + sci2 + eng2:
    print(inf + math + sci + eng)
else:
    print(inf2 + math2 + sci2 + eng2)
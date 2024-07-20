#2752

A,B,C=map(int,input().split())
print(min(A,B,C),A+B+C-max(A,B,C)-min(A,B,C),max(A,B,C))
N = int(input())
for i in range(N):
    print(" " * (N-i-1), end = "")
    print("*" * (i+1))
for j in range(N-1):
    print(" " * (j+1), end = "")
    print("*" * (N-1-j))
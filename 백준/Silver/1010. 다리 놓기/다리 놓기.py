import math

T = int(input())
for i in range(T):
    west,east = map(int,(input().split()))
    print(int(math.factorial(east)/(math.factorial(west) * math.factorial(east-west))))

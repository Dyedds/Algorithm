#2010
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
plugs = map(int, data[1:])

max_computer = sum(plugs) - N + 1

print(max_computer)

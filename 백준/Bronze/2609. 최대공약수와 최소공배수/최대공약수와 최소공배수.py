#2609번 최대공약수와 최소공배수
#num1, num2 는 입력 두 자연수
import math
num1, num2 = map(int,(input().split()))
print(math.gcd(num1,num2))
print(math.lcm(num1,num2))

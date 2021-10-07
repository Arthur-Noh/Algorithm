# 기초 수학 문제
# 백준 2609 최대공약수와 최소공배수
# 등급 실버 5

# 문제 해결 아이디어
# 유클리드 호제법을 사용하여 해결할 수 있다.

# 최대 공약수 GCD
# a 를 b 로 나눈 나머지 c 를 통해
# a 와 b의 최대공약수와 b 와 c의 최대공약수가 같다.
# a % b = c, b % c = 같은 최대공약수

# 최소 공배수 LCM
# 최소 공배수 = 두 자연수의 곱 / 최대공약수

import sys

# 두 개의 자연수 입력
a, b = map(int, sys.stdin.readline().split())


# 최대 공약수
def gcd(a, b):
    if b == 0:
        return a

    else:
        return gcd(b, a % b)


# 최소 공배수
def lcm(a, b):
    return int(a * b / gcd(a, b))


sys.stdout.write("{0}\n".format(gcd(a, b)))
sys.stdout.write("{0}\n".format(lcm(a, b)))

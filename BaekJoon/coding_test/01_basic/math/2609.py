# 코딩 테스트 준비 - 기초
# 백준 2609 최대공약수와 최소공배수
# 등급 실버 5

# 문제 해결 아이디어
# 유클리드 호제법을 사용하여 문제를 해결할 수 있다.

# 최대공약수 GCD
# a 를 b로 나눈 나머지 c를 통해
# a 와 b의 최대공약수는 b와 c의 최대공약수와 같다.

# 최소공배수 LCM
# 최소공배수 = 두 자연수의 곱 / 최대공약수

import sys

# a, b 입력
a, b = map(int, sys.stdin.readline().split())


def gcd(a, b):
    if a % b == 0:
        return b

    else:
        return gcd(b, a % b)


def lcm(a, b):
    return int(a * b / gcd(a, b))


print(gcd(a, b))
print(lcm(a, b))

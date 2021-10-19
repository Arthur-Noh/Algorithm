# 코딩 테스트 준비 - 기초
# 백준 10430 나머지
# 등급 브론즈 5

# 문제 해결 아이디어
# 주어진 식 그대로 풀이하면 된다.

import sys

# a, b, c 입력
a, b, c = map(int, sys.stdin.readline().split())

# 출력
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)

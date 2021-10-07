# 기초 수학 문제
# 백준 2460 지능형 기차 2
# 등급 브론즈 2

# 문제 해결 아이디어
# 역 순서대로 먼저 입력을 받고
# 현재 탑승 인원 - 이번 역의 내린 사람의 수 + 이번 역의 탑승객의 수 를 계산하여
# 가장 큰 값을 저장하여 MAX 출력하면 된다.

import sys

MAX = 0 # 최대 탑승객의 수
now = 0 # 현재 탑승객의 수

for i in range(10):
    o, i = map(int, sys.stdin.readline().split())
    now = now - o + i
    MAX = now if now > MAX else MAX

sys.stdout.write("{0}\n".format(MAX))

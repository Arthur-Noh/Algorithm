# 기초 수학 문제
# 백준 1292 쉽게 푸는 문제
# 등급 실버 5

# 문제 해결 아이디어
# 1 ~ 1000까지 밖에 없으니까 총 리스트는 46까지밖에 출력이 안된다.
# 따라서 이중 포문을 사용하여 i 는 46까지 반복을 하고
# j 는 i 까지 반복을 하여 i 를 배열에 입력받으면 된다.
# 그리고 구간의 합을 구하면 된다.

import sys

# 구간 변수 A, B
a, b = map(int, sys.stdin.readline().split())
arr = []  # 총 리스트

for i in range(46):
    for j in range(i):
        arr.append(i)

s = 0  # 합 변수

for i in range(a - 1, b):
    s += arr[i]

sys.stdout.write("{0}\n".format(s))

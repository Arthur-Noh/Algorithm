# 기초 수학 문제
# 백준 10870 피보나치
# 등급 브론즈 2

# 문제 해결 아이디어
# 먼저 기본 숫자를 대입해두고 피보나치 연산을 수행하여 배열에 대입한다.
# 그리고 그 마지막 피보나치 숫자를 출력하면 된다.

import sys

# 피보나치 수를 입력받을 배열(기본인자 0, 1)
arr = [0, 1]

# N 입력
n = int(sys.stdin.readline().rstrip())

# 피보나치 배열 입력
for i in range(2, n + 1):
    arr.append(arr[i - 1] + arr[i - 2])

# N 번째 피보나치 수 출력
sys.stdout.write("{0}\n".format(arr[n]))

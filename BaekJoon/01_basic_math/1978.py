# 기초 수학 문제
# 백준 1978 소수 찾기
# 등급 실버 4

# 문제 해결 아이디어
# 소수는 1과 자기 자신만을 약수로 가지는 수를 의미한다.
# 따라서 소수가 아닌 수를 찾으려면 2 ~ n - 1까지 나누었을때 나머지가 0인 수의 갯수를 구하면 된다.

import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
sosu = 0

for number in arr:
    error = 0  # 소수가 아닌 녀석을 체크하기 위한 변수

    if number > 1: # 만약에 입력받은 수가 1보다 크다면
        for i in range(2, number):  # 2부터 n - 1까지 나누었을 때
            if number % i == 0:  # 나눠지는 수가 존재한다면
                error += 1  # 그 수는 소수가 아니다.

        if error == 0:
            sosu += 1

sys.stdout.write("{0}\n".format(sosu))

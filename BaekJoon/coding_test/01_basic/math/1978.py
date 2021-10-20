# 코딩 테스트 준비 - 기초
# 백준 1978 소수 찾기
# 등급 실버 4

# 문제 해결 아이디어
# 소수는 1와 자기 자신만을 약수로 가지는 수를 의미한다.
# 1일때는 그냥 패스 하면 된다.
# 나머지는 2부터 나누기 시작해서 소수인지 찾으면 된다.

import sys
n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
count = 0
flag = True

for number in numbers:
    if number == 1:  # 1인 경우 다시 위로 올라감
        continue
    flag = True

    for i in range(2, number):  # 2부터 나누면서
        if number % i == 0:  # 나눠 떨어진다면
            flag = False  # 소수가 아니다
            break  # 바로 반복문 탈출

    if flag:  # 소수 인 경우
        count += 1

print(count)

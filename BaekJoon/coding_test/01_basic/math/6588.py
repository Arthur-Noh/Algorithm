# 코딩 테스트 준비 - 기초
# 백준 6588 골드바흐의 추측
# 등급 실버 1

# 문제 해결 아이디어
# 에라토스테네스의 체를 사용한다.
# 에라토스테네스의 체를 사용하여 최대 값까지의 모든 소수를 찾고
# 입력이 들어올 때 마다, i 번째 해당하는 소수와 n - i 번째 해당하는 소수가 True면
# 그 연산을 출력하면 된다.

import sys

max_t = 10 ** 6
prime = [True] * max_t

for i in range(2, int(max_t ** 0.5) + 1):   # 최대값의 제곱근 까지의 범위에서
    if prime[i]:                            # prime[i]가 True 일 때
        for j in range(i * 2, max_t, i):    # prime 의 두배 값 부터, 최대 값 까지 i 의 배수를 모두 False 로 변환한다.
            prime[j] = False

while True:
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        break

    flag = True  # 골드바흐가 틀리는 것을 찾기 위한 변수

    for i in range(3, max_t):                               # 4부터 시작하니 소수인 3부터
        if prime[i] and prime[n - i]:                       # i 번째 소수와 n - i 번째 소수가 True 이면
            print("{0} = {1} + {2}".format(n, i, n - i))    # 두 값의 합으로 나타낼 수 있다. 출력
            flag = False
            break

    if flag:
        print("Goldbach's conjecture is wrong.")

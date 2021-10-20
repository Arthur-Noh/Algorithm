# 코딩 테스트 준비 - 기초
# 백준 1929 소수 구하기
# 등급 실버 2

# 문제 해결 아이디어
# 그냥 입력 받고 1과 자기 자신만을 약수로 가지는 값을 출력하면 된다.
# 일반적인 식으로 풀면 시간초과가 발생하는데
# "에라토스테네스의 체"를 사용하면 된다.
# 에라토스테네스의 체 란?
# 소수를 찾는 방법인데, 일정 범위 내 수열에서 배수들을 제거해 소수만 남기는 방법이다.
# 주어진 수에 제곱근 범위 까지만 연산하면 더 이상의 연산은 무의미하다.

import sys

m, n = map(int, sys.stdin.readline().split())


def isprime(m, n):
    n += 1                                  # for 문 사용을 위한 n += 1
    prime = [True] * n                      # n개의 [True]가 있는 리스트를 만들고
    for i in range(2, int(n ** 0.5) + 1):   # n의 제곱근 까지만 검사를 한다.
        if prime[i]:                        # prime[i] 가 True 일때
            for j in range(2 * i, n, i):    # prime 내에 있는 i 의 모든 배수들을 False 로 변환한다.
                prime[j] = False

    for i in range(m, n):
        if i > 1 and prime[i]:              # 1 이상이면서 남은 소수들을 출력하면 된다.
            print(i)


isprime(m, n)

# 코딩 테스트 준비 - 기초
# 백준 15654 N 과 M(5)
# 등급 실버 3

# 문제 해결 아이디어
# 백트래킹 방식으로 해결할 수 있다.
# 이번에는 입력이 1 ~ n 까지가 아니라 정수로 따로 입력을 받으므로
# numbers 라는 리스트를 받게 한다.
# 수열이 사전 순으로 증가하게 만들기 위해서 numbers를 오름차순 정렬을 수행한다.
# 이번에는 중복을 허용하지 않기 때문에 배열 s 에 중복되지 않는 값들만 입력 받아서
# 다음 dfs 로 보내준다.

import sys
n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
s = []

numbers.sort()


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for number in numbers:
        if number not in s:
            s.append(number)
            dfs()
            s.pop()


dfs()

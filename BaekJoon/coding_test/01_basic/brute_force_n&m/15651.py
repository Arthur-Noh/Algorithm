# 코딩 테스트 준비 - 기초
# 백준 15651 N 과 M(3)
# 등급 실버 3

# 문제 해결 아이디어
# 백 트래킹으로 문제를 해결할 수 있다.
# 중복을 허용하기 때문에 조건문을 제거하고 실행하면 된다.

import sys
n, m = map(int, sys.stdin.readline().split())
s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()


dfs()

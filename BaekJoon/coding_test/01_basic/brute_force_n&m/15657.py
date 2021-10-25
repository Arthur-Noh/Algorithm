# 코딩 테스트 준비 - 기초
# 백준 15657 N 과 M(8)
# 등급 실버 3

# 문제 해결 아이디어
# 기존 해결 방식과 동일하고, 백트래킹 방식으로 해결한다.
# 먼저 numbers를 입력받고 오름차순으로 정렬한다.
# 그리고 dfs 를 선언해서 s 리스트에 numbers 값을 순차적으로 입력 받는다.
# 그러나 다음 값은 항상 자신보다 크거나 같아야 하므로 i 라는 값을 시작값으로 하여 dfs를 선언해준다.

import sys
n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
s = []

numbers.sort()


def dfs(start):
    if len(s) == m:
        print(' '.join((map(str, s))))
        return

    for i in range(start, n):
        s.append(numbers[i])
        dfs(i)
        s.pop()


dfs(0)

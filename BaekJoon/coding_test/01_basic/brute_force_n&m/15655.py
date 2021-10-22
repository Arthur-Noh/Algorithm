# 코딩 테스트 준비 - 기초
# 백준 15655 N 과 M(6)
# 등급 실버 3

# 문제 해결 아이디어
# 기존과 동일하게 하되 백트래킹으로 문제를 해결하면 된다.
# 먼저 numbers를 오름차순 정렬을 수행한다.
# dfs로 값을 입력 받되, start를 변수로 받아서 반복문의 시작 지점으로 설정한다.
# 반복문을 수행하면서 start를 하나 늘린 값을 다음 dfs로 반복해서 넘겨주어 실행하면 된다.

import sys
n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
s = []

numbers.sort()


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n):
        s.append(numbers[i])
        dfs(i + 1)
        s.pop()


dfs(0)

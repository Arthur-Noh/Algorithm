# 코딩 테스트 준비 - 기초
# 백준 15652 N 과 M(4)
# 등급 실버 3

# 문제 해결 아이디어
# 시작 값부터 순차적으로 출력을 할 것이기 때문에
# 시작 지점을 dfs의 입력으로 받아 리스트 추가 구문 i의 시작 지점으로 삼으면 된다.
# 그러면서 중복을 허용하기 때문에 반복문 부분에서 dfs의 값을 넘겨줄때 i 값으로 넘겨주면 된다.

import sys
n, m = map(int, sys.stdin.readline().split())
s = []


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        s.append(i)
        dfs(i)
        s.pop()


dfs(1)

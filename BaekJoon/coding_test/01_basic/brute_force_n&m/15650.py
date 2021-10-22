# 코딩 테스트 준비 - 기초
# 백준 15650 N 과 M(2)
# 등급 실버 3

# 문제 해결 아이디어
# 이 문제는 DFS의 일종인 백 트래킹으로 해결할 수 있다.
# 앞서 나온 숫자들을 다시 볼 필요가 없으므로 변수중에 시작하는 위치의 변수를 추가해서
# dfs를 수행할 때 시작 값을 넘겨서 내부에서 수행하면 된다.


import sys
n, m = map(int, sys.stdin.readline().split())
s = []


def dfs(start):  # 시작 값을 변수로 입력 받아서
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):  # 시작 값부터 목표값 n까지 반복을 한다.
        if i not in s:  # 만약에 배열에 그 값이 없다면
            s.append(i)  # 리스트에 값을 추가해 주고
            dfs(i + 1)  # 다음 값부터 시작하도록 시작 값을 넘겨주면 된다.
            s.pop()


dfs(1)

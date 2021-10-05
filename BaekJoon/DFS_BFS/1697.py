# DFS/BFS 문제
# 백준 1697번
# 등급 실버 1

# 문제 해결 아이디어
# BFS로 해결할 수 있다.
# BFS로 해결 가능한 모든 경우의 수를 체크하면 되는 문제이다.
# (다음 값, 다음값으로 이동하는데 걸린 횟수)를 짝으로 만들어서
# 모든 경우의 수를 체크하여 돌려주는 알고리즘이다.

# 아니 근데 BFS로 풀면 메모리 초과 오류가 발생한다.
# 그래서 리스트의 길이를 반으로 줄이고 나머지 반쪽 가지고 풀이를 해보았다.
# 여기서 distance 는 visited와 같은 기능을 수행한다고 보면 된다.

# 참고
# https://wook-2124.tistory.com/273

from collections import deque
import sys

a, b = map(int, sys.stdin.readline().split())

MAX = 10 ** 5
distance = [0] * (MAX * 1)


def bfs():
    queue = deque()
    queue.append(a)

    while queue:
        x = queue.popleft()

        if x == b:
            print(distance[x])
            break

        for i in (x + 1, x - 1, x * 2):
            if 0 <= i <= MAX and not distance[i]:
                distance[i] = distance[x] + 1
                queue.append(i)

bfs()

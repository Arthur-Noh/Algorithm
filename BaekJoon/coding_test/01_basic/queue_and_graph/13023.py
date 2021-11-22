# 코딩 테스트 준비 - 기초
# 백준 13023 ABCDE
# 등급 골드 5

# 문제 해결 아이디어
# DFS 백트래킹 방식으로 만들면 된다.
# 인접 노드를 가르키는 그래프 형식으로 만들고
# 방문 했는지 안했는지를 따져가며 해결하면 된다.

import sys

n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n)]
visited = [False] * n

# 그래프를 인접 리스트 방식으로 만든다.
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(idx, count):
    if count == 4:  # 깊이가 4 이상이라는 것은 ABCDE가 모두 친구라는 뜻이므로 바로 탈출
        print(1)  # 이렇게 안하면 자꾸 시간초과가 뜸 
        exit()

    for i in arr[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, count + 1)
            visited[i] = False


# 시작지점을 변경하면서 dfs를 호출한다.
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)

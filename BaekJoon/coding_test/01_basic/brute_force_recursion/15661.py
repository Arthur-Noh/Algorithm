# 코딩 테스트 준비 - 기초
# 백준 15661 링크와 스타트
# 등급 실버 1

# 문제 해결 아이디어
# 백트래킹으로 해결해본다.

import sys
n = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
team = [False] * (n + 1)
result = 10 ** 9


def dfs(t, count):  # t : 선택된 팀의 갯수, count : 트리의 깊이
    global result

    # 종료조건 :
    # 트리의 깊이가 n = 4 라면, count == n 일때 끝까지 모든 팀을 본 것이므로 stop
    if count == n:
        return

    # 스타트와 링크 팀의 차이를 가장 작게하는 값을 찾는 것이다.
    # 따라서 스타트팀과 링크팀은 n의 반정도를 선택하면 나머지는 자동으로 선택된다.
    # ex) 1, 5의 차이는 5, 1의 차이와 같다.
    if t > int(n//2) + 1:
        return

    # 실행 조건 : 팀이 하나 이상 선택되었다면 비교 수행
    if t >= 1:
        team1, team2 = 0, 0

        for i in range(n):
            for j in range(n):
                if team[i] and team[j]:
                    team1 += board[i][j]
                elif not team[i] and not team[j]:
                    team2 += board[i][j]

        result = min(result, abs(team1 - team2))

    # 실행 조건 : 팀이 하나 이상 선택 되지 않더라도, 모든 경우의 수를 찾아본다.
    # 팀을 선택한 경우
    team[count] = True
    dfs(t + 1, count + 1)
    # 팀을 선택하지 않는 경우
    team[count] = False
    dfs(t, count + 1)


dfs(0, 0)
print(result)

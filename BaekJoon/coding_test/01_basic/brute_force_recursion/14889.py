# 코딩 테스트 준비 - 기초
# 백준 14889 스타트와 링크
# 등급 실버 3

# 문제 해결 아이디어
# S12 + S21 - S34 + S43의 차이가 가장 작은 값을 찾아라
# 최대 값은 아무 값이나 입력을 했다.
# 먼저 1번 팀과 2번 팀을 나눠서 찾는 방식을 사용하였다.
# dfs로 n /2 명의 사람을 선택해 팀을 나눈다.
# team이 0 인지 1인지에 따라 팀이 나뉘고 각각 팀에 해당하는 값을 더해준다.
# 팀의 능력치 합의 차이가 최소가 되는 값을 출력하면 된다.

import sys
n = int(sys.stdin.readline().rstrip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
team = [0] * n
result = 201


def dfs(index, count):  # 반복을 시작할 값과 재귀가 반복된 횟수를 인자로 받는다.
    global result

    # 종료 조건 : 4번 반복을 하면 각각의 팀 점수를 구하고 차이의 최솟값을 result에 넣는다.
    if count == n // 2:
        team_1, team_2 = 0, 0

        for i in range(n):
            for j in range(n):
                # 2팀은 1/ 1팀은 0이므로
                # 1, 1 이거나 0, 0일때의 값을 팀 값에 더해준다.
                if team[i] and team[j]:
                    team_1 += board[i][j]
                elif not team[i] and not team[j]:
                    team_2 += board[i][j]
        result = min(result, abs(team_1 - team_2))
    
    # 실행 조건
    # 반복을 시작할 값을 넣고 n - 1까지 반복한다.
    # 같은 1 이라면 그냥 다시 위로 올라가고 0번이라면 1을 대입하여 다시 dfs를 수행한다.
    for i in range(index, n):
        if team[i]:
            continue
        team[i] = 1
        dfs(i + 1, count + 1)
        team[i] = 0


dfs(0, 0)
print(result)

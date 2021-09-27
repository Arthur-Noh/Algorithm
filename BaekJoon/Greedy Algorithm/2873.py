# 그리디 알고리즘
# 백준 2873번
# 등급 플레티넘 3

# 문제 해결 아이디어
# 기쁨의 합이 최대가 될 수 있게 해라.
# 합이 최대가 되기 위해서는 최대한 많은 칸을 방문하면 된다.
# 행 또는 열의 갯수가 홀수라면 모든 지점을 방문할 수 있다.
# 행과 열의 갯수가 짝수라면 단 한 점을 제외하고 모든 지점을 방문할 수 있다.

import sys

row, column = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

if row % 2 == 1:
    sys.stdout.write(('R' * (column - 1) + 'D' + 'L' * (column - 1) + 'D') * (row // 2) + 'R' * (column - 1))
elif column % 2 == 1:
    sys.stdout.write(('D' * (row - 1) + 'R' + 'U' * (row - 1) + 'R') * (column // 2) + 'D' * (row - 1))
elif row % 2 == 0 and column % 2 == 0:
    # 건너뛸 위치를 정한다.
    low = 1000
    position = [-1, -1]

    for i in range(row):
        if i % 2 == 0:
            for j in range(1, c, 2):
                if low > ground[i][j]:
                    low = ground[i][j]
                    position = [i, j]

        else:
            for j in range(0, c, 2):
                if low > ground[i][j]:
                    low = ground[i][j]
                    position = [i, j]

    res = ('D' * (row - 1) + 'R' + 'U' * (row - 1) + 'R') * (position[1] // 2)
    x = 2 * (position[1] // 2)
    y = 0
    xbound = 2 * (position[1] // 2) + 1

    while x != xbound or y != (row - 1):
        if x < xbound and [y, xbound] != position:
            x += 1
            res += 'R'
        elif x == xbound and [y, xbound - 1] != position:
            x -= 1
            res += 'L'

        if y != row - 1:
            y += 1
            res += 'D'

    res += ('R' + 'U' * (row - 1) + 'R' + 'D' * (row -1)) * ((column - position[1] - 1) // 2)

    print(res)

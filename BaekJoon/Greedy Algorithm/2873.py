# 그리디 알고리즘
# 백준 2873번
# 등급 플레티넘 3

# 문제 해결 아이디어
# 기쁨의 합이 최대가 될 수 있게 해라.
# 합이 최대가 되기 위해서는 최대한 많은 칸을 방문하면 된다.
# 행 또는 열의 갯수가 홀수라면 모든 지점을 방문할 수 있다.
# 행과 열의 갯수가 짝수라면 단 한 점을 제외하고 모든 지점을 방문할 수 있다.

import sys

# 행과 열 입력
r, c = map(int, sys.stdin.readline().split())

# 지도 입력
m = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

if r % 2 == 1: # 행의 갯수가 홀수일 때
    sys.stdout.write(('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (r // 2) + 'R' * (c - 1))
elif c % 2 == 1: # 열의 갯수가 홀수일 때
    sys.stdout.write(('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (c // 2) + 'D' * (r - 1))

elif r % 2 == 0 and c % 2 == 0: # 이 알고리즘에서는 아래로 찾는 형식으로 구현하였다.
    lowest = 1001 # 최저값을 찾기 위해 초기화
    lowPosition = [-1, -1] # 최저값의 위치

    for i in range(r):
        if i % 2 == 0: # 최저값의 위치가 짝수 행 일때
            for j in range(1, c, 2): # 최저값이 홀수 열(체크 O)에 해당하는 값이면
                if lowest > m[i][j]:
                    lowest = m[i][j]
                    lowPosition = [i, j]
        else: # 최저값의 위치가 홀수 행 일때
            for k in range(0, c, 2): # 최저값이 짝수 열(체크 O)에 해당하는 값이면
                if lowest > m[i][k]:
                    lowest = m[i][k]
                    lowPosition = [i, k]

    # 최저값이 존재하는 열 바로 직전까지 result에 DD..RUU..R 을 저장한다.
    result = ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (lowPosition[1] // 2)

    # x : 건너뛸 값의 열, 체크가 없는 값 
    # y : 행
    # xbound : 건너뛸 값, +1 을 하는 이유는 체크에 해당하는 값만 제외시킬 수 있기 때문이다.
    x = 2 * (lowPosition[1] // 2)
    y = 0
    xbound = 2 * (lowPosition[1] // 2) + 1
    
    while x != xbound or y != r - 1:
        if x < xbound and [y, xbound] != lowPosition:
            x += 1
            result += 'R'
        elif x == xbound and [y, xbound - 1] != lowPosition:
            x -= 1
            result += 'L'

        if y != r - 1:
            y += 1
            result += 'D'

    result += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r - 1)) * ((c - lowPosition[1] - 1) // 2)

    print(result)

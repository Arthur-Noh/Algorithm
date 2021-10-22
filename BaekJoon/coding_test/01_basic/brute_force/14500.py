# 코딩 테스트 준비 - 기초
# 백준 14500 테트로미노
# 등급 골드 5

# 문제 해결 아이디어
# 참고 : https://jeongchul.tistory.com/670
# 테트리스의 모든 모양에 대하여 계산을 진행해보면 된다.
# 회전과 대칭에 따라 테트리스의 모양은 총 19개가 나오게 된다.
# 정의한 테트로미노의 19가지 모양에 대해 4가지 블록의 (X, Y)를 정의한다.
# solve() 모든 board의 위치에서 테트로미노를 놓고 합산한 값을 찾는 find()를 호출한다.
# find()에서는 주어진 좌표 x, y에 대해 테트로미노 19가지 모양을 놓고 계산한다.
# 테트로미노는 4가지 블록으로 구성되기 때문에 각 블록을 놓았을 때, x, y 좌표를 계산하고 합산한 값을 구하낟.
# 만약 현재 위치에서 테트로미노가 borad 바깥으로 나가게 된다면 index error이 발생하므로 try, except IndexError에 대한 처리를 한다.
# except가 발생한다면 continue로 다음 블럭을 계산하게 한다.
# 최종적으로 최대값을 max로 비교하여 저장한다.

import sys

# 입력
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
tetromino = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (1, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 1), (1, 1), (2, 1), (2, 0)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 1), (0, 2)],
    [(1, 0), (1, 1), (0, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 0)],
    [(0, 1), (1, 1), (1, 0), (2, 1)],
    [(0, 1), (1, 1), (1, 0), (2, 0)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (1, 1), (0, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)]
]
answer = 0


def find(x, y):
    global answer
    for i in range(19):
        result = 0
        for j in range(4):
            try:
                next_x = x + tetromino[i][j][0]  # x 좌표
                next_y = y + tetromino[i][j][1]  # y 좌표
                result += graph[next_x][next_y]
            except IndexError:
                continue
        answer = max(answer, result)


def solve():
    for i in range(n):
        for j in range(m):
            find(i, j)

solve()
print(answer)

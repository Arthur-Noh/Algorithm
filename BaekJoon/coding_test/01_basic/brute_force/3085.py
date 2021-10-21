# 코딩 테스트 준비 - 기초
# 백준 3085 사탕 게임
# 등급 실버 4

# 문제 해결 아이디어
# 인접한 두 칸을 골라 사탕을 교환하고 전체 보드를 탐새가여 같은 색으로 이루어진 사탕 개수를 확인한다.
# 사탕의 최대 개수 r 보다 구한 사탕 개수 c가 더 크면 r을 c로 바꾼다
# 교환한 사탕을 원래대로 되돌려 놓는다.
# 1, 2, 3 과정을 사탕을 교환하는 모든 경우에 실행한다.
# 최대 사탕의 개수를 출력한다.

import sys
n = int(sys.stdin.readline().rstrip())
candys = [list(sys.stdin.readline()) for _ in range(n)]
result = 0


def width():  # 열을 중심으로 교환한 캔디를 비교한다.
    global result

    for i in range(n):
        c = 1
        for j in range(1, n):
            if candys[i][j] == candys[i][j - 1]:
                c += 1
            else:
                if result < c:
                    result = c
                c = 1

        if result < c: # 한줄이 모두 같은 경우 수행
            result = c


def heigth():  # 행을 중심으로 교환할 캔디를 비교한다.
    global result

    for i in range(n):
        c = 1
        for j in range(1, n):
            if candys[j][i] == candys[j - 1][i]:
                c += 1
            else:
                if result < c:
                    result = c
                c = 1

        if result < c:  # 한줄이 모두 같은 경우 수행
            result = c


for i in range(n):  # 열을 중심으로 캔디를 교환
    for j in range(1, n):
        candys[i][j], candys[i][j - 1] = candys[i][j - 1], candys[i][j]  # 사탕의 위치를 바꾸고
        width()
        heigth()
        candys[i][j], candys[i][j - 1] = candys[i][j - 1], candys[i][j]  # 다시 사탕의 위치를 원래대로 돌려주기

for i in range(n):  # 행을 중심으로 캔디를 교환
    for j in range(1, n):
        candys[j][i], candys[j - 1][i] = candys[j - 1][i], candys[j][i]
        width()
        heigth()
        candys[j][i], candys[j - 1][i] = candys[j - 1][i], candys[j][i]

print(result)

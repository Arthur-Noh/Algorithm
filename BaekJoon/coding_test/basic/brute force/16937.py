# 코딩 테스트 준비 - 기초
# 백준 16937 두 스티커
# 등급 실버 4

# 문제 해결 아이디어
# 모눈종이에 스티커를 2개를 붙이기 때문에 네가지 경우를 고려할 수 있다.
# 둘다 회전 x, 1번만 회전, 2번만 회전, 둘다 회전
# 스티커의 요소 가로1, 세로1, 가로2, 세로2 로 나눠서 각각을 돌려보았을 때
# 스티커의 가로 세로를 넘지 않으면서 최대값을 가지는 값을 찾으면 된다.

import sys
# 모눈종이 H, W 입력
h, w = map(int, sys.stdin.readline().split())

# 스티커의 수 N
n = int(sys.stdin.readline().rstrip())

# 각 스티커의 크기 입력
sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 모눈종이에 붙은 스티커의 최대 넓이
result = 0

for i in range(n):
    for j in range(i + 1, n):  # 옆으로 긴 직사각형으로 요소를 나눈다.
        r1 = max(sticker[i][0], sticker[i][1])  # 첫번째 스티커의 행
        c1 = min(sticker[i][0], sticker[i][1])  # 첫번째 스티커의 열
        r2 = max(sticker[j][0], sticker[j][1])  # 두번째 스티커의 행
        c2 = min(sticker[j][0], sticker[j][1])  # 두번째 스티커의 열

        if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):  # 둘 다 회전하지 않은 경우
            result = max(result, r1 * c1 + r2 * c2)
        if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):  # 1번만 회전한 경우
            result = max(result, r1 * c1 + r2 * c2)
        if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):  # 2번만 회전한 경우
            result = max(result, r1 * c1 + r2 * c2)
        if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):  # 둘 다 회전한 경우
            result = max(result, r1 * c1 + r2 * c2)

sys.stdout.write("{0}\n".format(result))

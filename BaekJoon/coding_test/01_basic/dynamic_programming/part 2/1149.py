# 코딩 테스트 준비 - 기초
# 백준 1149 RGB거리
# 등급 실버 2

# 문제 해결 아이디어
# 첫번째는 계산하지 않고 두번째 집의 색칠 비용부터 계산을 시작한다.
# 두번째 집부터 빨간집인 경우, 초록집인 경우, 파랑집인 경우를 계산하는데
# 그 이전의 값들 중에서 같은 색을 제외한 최소 값을 더해주는 것을 반복한다.
# 결국에는 빨강, 초록, 파랑 집을 선택한 모든 경우에 대해 최솟값만 더해진다.
# 그 마지막 집의 누적 비용에서 최솟값을 선택하여 출력하면 된다.

import sys
n = int(sys.stdin.readline().rstrip())
rgb = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    # 빨간집
    rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + rgb[i][0]
    # 초록집
    rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + rgb[i][1]
    # 파란집
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + rgb[i][2]

print(min(rgb[n - 1]))

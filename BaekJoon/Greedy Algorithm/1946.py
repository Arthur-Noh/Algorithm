# 그리디 알고리즘
# 백준 1946번
# 등급 실버 1

# 문제 해결 아이디어
# 면접자들의 서류점수(1차)를 기준으로 오름차순으로 정렬한 뒤, 면접 점수로 풀면 된다.
# 만약 A가 1, 4을 받고, B는 2, 3을 받았을 경우
# B는 A 보다 1차 점수는 낮지만 2차 점수가 높아 합격한다.
# 이제 B의 2차 점수를 기준으로 다음 사람을 판별하면 된다.

# 가장 먼저 서류점수(1차)를 기준으로 모든 면접자들을 오름차순으로 정렬한다.
# 서류점수(1차)에서 1등을 한 사람은 무조껀 합격하므로
# 합격자 수에 1명(서류점수 1등)을 반드시 포함하고, 그 1명의 면접점수(2차)를 기준 대상으로 삼는다.
# 다음 면접자(서류점수 2등)의 면접등수(2차)가 서류점수 x-1등 보다 낮은 경우
# 합격자 1명 추가, 해당 면접자의 2차 점수를 기준으로 다시 다음 등수비교를 실행하면 된다.

import sys

t = int(sys.stdin.readline())

for i in range(t):
    count = 1
    people = []

    n = int(sys.stdin.readline())
    for i in range(n):
        paper, interview = map(int, sys.stdin.readline().split())
        people.append([paper, interview])

    people.sort()
    max = people[0][1]

    for i in range(1, n):
        if max > people[i][1]:
            max = people[i][1]
            count += 1

    print(count)

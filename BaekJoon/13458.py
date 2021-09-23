# 그리디 알고리즘
# 백준 13458번
# 등급 브론즈 2

# 문제 해결 아이디어
# 시험장에 필요한 감독관의 최솟값을 구하면 된다.
# 간단하게 생각하면 된다.
# 1) 학생 수가 1명 이상이라면 총 감독관을 먼저 뺀다.
# 2) 1)을 하고도 학생수가 1명 이상이라면 부 감독관 만큼 나눠준 뒤 뺀다.
# 3) 2)를 하고도 학생수가 1명 이상이라면 감독관을 한명 더 추가한다.
# 위를 반복하면 금방 구할 수 있다.

import sys
input = sys.stdin.readline

test_site = int(input())
students = list(map(int, input().split()))
mainSuper, subSuper = map(int, input().split())

needSuper = 0

for i in range(test_site):
    if students[i] > 0:
        students[i] -= mainSuper
        needSuper += 1

    if students[i] > 0:
        needSuper += students[i]//subSuper
        if students[i] % subSuper != 0:
            needSuper += 1

print(needSuper)

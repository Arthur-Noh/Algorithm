# 그리디 알고리즘
# 백준 4796번
# 등급 실버 5

# 문제 해결 아이디어
# 연속하는 P 일 중에, L 일을 사용할 수 있다. 휴가는 V 일이다.
# 연속하는 8 일 중에, 5 일을 사용할 수 있고, 휴가는 20일 인 경우
# 5일 휴가 - 3일 X - 5일 휴가 - 3일 X - 4일(휴가의 나머지 일수) = 14일

# 연속하는 P일을 꽉 채워서 사용할 수 있는 갯수 : V // P
# 다 채우지 못하고 남은 휴가일 수 : V % P
# 만약 남은 휴가일 V % P 이 사용가능한 L 일 보다 큰 경우 : L 일 출력

import sys

case = 0

while True:
    l, p, v = map(int, sys.stdin.readline().split())
    case += 1

    full_day = 0
    rest_day = 0

    if l + p + v == 0:
        break

    full_day = v // p
    rest_day = min(v % p, l)

    print("Case {0}: {1}".format(case, full_day * l + rest_day))

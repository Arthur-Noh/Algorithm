# 코딩 테스트 준비 - 기초
# 백준 16917 양념 반 후라이드 반
# 등급 브론즈 3

# 문제 해결 아이디어
# 한 마리씩 사는 경우가 반반으로 두마리 사는 경우보다 쌀 경우 - 그냥 구매
# 아닌 경우 반반으로 한마리씩 구매
# 그리고 남은 나머지는 일반으로 구매하면 된다.

import sys
a, b, c, x, y = map(int, sys.stdin.readline().split())

if a + b < c * 2:
    print(a * x + b * y)

else:
    m = min(x, y)
    print(c*m*2 + min(c*2, a)*max(0, x-m) + min(c*2, b)*max(0, y-m))

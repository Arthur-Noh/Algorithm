# 코딩 테스트 준비 - 기초
# 백준 11727 2 * n 타일링 2
# 등급 실버 3

# 문제 해결 아이디어
# n = 1 - 1 개
# n = 2 - 3 개
# n = 3 - 5 개
# n = 4 - 11 개
# 규칙성 찾기
# n = (n - 1) + (n - 2) * 2 가 성립한다.

import sys
# 경우의 수
s = [0, 1, 3]

# 바텀 업
# 시간 복잡도는 O(N)
for i in range(3, 1001):
    s.append(s[i - 1] + s[i - 2] * 2)

# 입력
n = int(sys.stdin.readline().rstrip())

print(s[n] % 10007)

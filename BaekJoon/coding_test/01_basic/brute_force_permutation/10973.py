# 코딩 테스트 준비 - 기초
# 백준 10973 이전 순열
# 등급 실버 3

# 문제 해결 아이디어
# s[i] > s[i + 1]이 성립하는 지점 x 를 찾는다. (최댓값을 찾는다)
# - 없다면 오름차순 정렬이 되어있다는 뜻이다.
# 인덱스 x 이후 값들 중 s[x] > s[y]이 성립하는 y 을 찾는다.
# x 와 y 의 자리의 값을 서로 바꾼다.
# 인덱스 x 이후의 값들은 내림차순으로 정렬해준다.

import sys
n = int(sys.stdin.readline().rstrip())
s = list(map(int, sys.stdin.readline().split()))
x = -1

# s[i + 1] < s[i] 인 최댓값 지점 찾기
for i in range(n - 1):
    if s[i] > s[i + 1]:
        x = i

if x == -1:  # 오름차순 정렬인 경우 -1  출력
    print(-1)
else:  # 내림차순 정렬인 경우
    # 바뀌는 다음 지점부터 n 까지 탐색하면서
    # s[x] > s[i] 보다 커지는 지점의 최댓값을 찾는다. (y)
    for i in range(x + 1, n):
        if s[i] < s[x]:
            y = i

    s[x], s[y] = s[y], s[x]

    s = s[:x + 1] + sorted(s[x + 1:], reverse=True)
    print(*s)

# 코딩 테스트 준비 - 기초
# 백준 1476 날짜 계산
# 등급 실버 5

# 문제 해결 아이디어
# 부르트 포스를 사용하여 해결할 수 있다.
# 수들을 입력을 받고 각각에 대응하는 변수 i, j, k 를 만든다.
# i, j, k 를 1씩 더해가는데 각 대응 변수들이 최고 값 16, 29, 20 을 만나면 다시 1로 초기화를 시켜준다.
# 계속 반복하면서 최종적으로 esm과 ijk가 같이질 때까지의 횟수를 계산하면 된다.

import sys
e, s, m = map(int, sys.stdin.readline().split())
count = 1
i, j, k = 1, 1, 1

while True:
    if i == e and j == s and k == m:
        break

    i += 1
    j += 1
    k += 1
    count += 1

    if i == 16:
        i = 1
    if j == 29:
        j = 1
    if k == 20:
        k = 1

print(count)

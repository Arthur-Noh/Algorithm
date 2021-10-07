# 기초 수학 문제
# 백준 2693 N번째 큰 수
# 등급 실버 5

# 문제 해결 아이디어
# 내림차순 정렬을 수행한 뒤 3번째 요소를 출력 시키면 된다.

# 첫 줄에 테스트 케이스 T가 주어진다.
# 배열 T의 원소 10개가 공백으로 구분되어 주어진다.
# 각 배열에서 3번째 큰 값을 출력한다.
# 한 줄에 하나씩 출력한다.

import sys

# 테스트 케이스 T
t = int(sys.stdin.readline().rstrip())

# N 번째 큰 값 출력
for i in range(t):
    n = list(map(int, sys.stdin.readline().split()))
    n.sort(reverse=True)
    print(n[2])

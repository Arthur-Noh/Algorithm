# 코딩 테스트 준비 - 기초
# 백준 6603 로또
# 등급 실버 2

# 문제 해결 아이디어
# combinations 함수를 호출하면 자동으로 사전순으로 정렬해주기 떄문에 간단하게 해결할 수 있다.


from itertools import combinations
import sys

while True:
    s = list(map(int, sys.stdin.readline().split()))
    if s[0] == 0:
        break

    del s[0]
    s = list(combinations(s, 6))

    for i in s:
        for j in i:
            print(j, end= ' ')
        print()
    print()

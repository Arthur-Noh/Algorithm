# 코딩 테스트 준비 - 기초
# 백준 10972 다음 순열
# 등급 실버 3

# 문제 해결 아이디어
# 참고 : https://rimkongs.tistory.com/m/212?category=815698
# next permutation 알고리즘을 사용하면 된다.
# 사전순으로 정렬한 배열 A 가 있다면
# A[i - 1] < A[i]로 바뀌는 지점을 찾는 것이 중요하다.
# 해당 지점 index 를 찾았을 때, 그 인덱스 값을 저장하고 x
# A[i - 1] 과 A[i]를 swap 한다.
# 그리고 찾아진 x 지점까지는 그대로 순열에 입력하고
# 다음 x + 1 ~ 끝까지는 오름차순으로 정렬하여 순열에 입력하면 된다.

import sys
n = int(sys.stdin.readline().rstrip())
s = list(map(int, sys.stdin.readline().split()))
x = 0  # 바뀌는 지점의 인덱스 저장 변수

# s[i - 1] < s[i] 지점 찾기
for i in range(n - 1, 0, -1):
    if s[i - 1] < s[i]:
        x = i - 1
        break

for i in range(n - 1, 0, -1):
    # 바뀌는 지점 부터 다시 수행하면 된다.
    # s[x]와 s[i] 두 값을 swap 하고
    # 0 ~ x 까지는 그대로, x + 1 ~ 끝까지는 오름차순 정렬 수행
    if s[x] < s[i]:
        s[x], s[i] = s[i], s[x]
        s = s[:x + 1] + sorted(s[x + 1:])
        print(*s)
        exit()

print(-1)

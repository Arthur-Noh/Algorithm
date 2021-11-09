# 코딩 테스트 준비 - 기초
# 백준 14002 가장 긴 증가하는 부분 수열 4
# 등급 골드 4

# 문제 해결 아이디어
# 최대 리스트의 길이를 찾는 방법은 기존의 방법과 동일하다.
# 그러나 문제는 수열의 길이까지 출력한다는 의미인데
# 일단 먼저 최대 리스트의 길이를 저장하는 dp 리스트를 만든다.
# dp 리스트의 뜻은 해당 위치의 값이 최대 값일때 부분수열의 최대 길이를 저장하는 리스트이다.
# 만약 입력이 10 20 10 30 20 50 이라면
# dp = {1 2 1 3 1 4} 이렇게 저장이 될 것이다.

# 이제 순서대로 출력하는 출력문을 만들 것인데,
# dp의 최댓값을 가지는 변수 order을 만들고 순차적으로 줄여가며 값을 출력한다.
# 반복문을 돌려 맨 뒤부터 순차로 하나씩 줄여가며 값을 찾아간다.
# order 은 4 3 2 1 순서로 줄어들 것이며 만약 dp[i] 가 order 값과 같다면
# 출력할 리스트 lst에 추가하고 order을 하나 줄인다.
# 오름차순 출력이므로 lst를 정렬하고 출력하면 된다.


import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
dp = [1] * n  # 항상 자기 자신을 포함하게 되므로 1로 먼저 초기화

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

order = max(dp)
lst = []

for i in range(n - 1, -1, -1):
    if dp[i] == order:
        lst.append(a[i])
        order -= 1

lst.reverse()
print(*lst)

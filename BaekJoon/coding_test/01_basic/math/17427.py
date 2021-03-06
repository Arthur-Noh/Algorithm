# 코딩 테스트 준비 - 기초
# 백준 17427 약수의 합 2
# 등급 실버 2

# 문제
# 두 자연수 A, B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다.
# 자연수 A의 약수의 합은 모든 약수를 더한 값이고, f(A)로 표현한다.
# x 보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값은 g(x)로 표현한다.

# 첫째 줄에 자연수 N 이 주어질 때 g(N)을 출력하라

# 문제 해결 아이디어
# N의 배수는 항상 N을 약수로 가진다.
# 그러므로 N 이하의 자연수 중에 i 를 약수로 갖는 개수는 N/i 개 이다.
# 이 경우에는 시간 복잡도가 O(N) 이다.

import sys
n = int(sys.stdin.readline().rstrip())
result = 0

for i in range(1, n + 1):
    # i 의 배수의 갯수 = i 를 약수로 갖는 수의 갯수
    result += (n//i) * i
    
print(result)

# 코딩 테스트 준비 - 기초
# 백준 1037 약수
# 등급 실버 5

# 문제 해결 아이디어
# 간단하게 생각하면 약수를 오름차순 정렬을 하고
# 제일 작은 수와 제일 큰 수를 곱해주면 된다.
# N의 약수를 모두 주어지기 때문에 그 둘을 곱하면 N이 나온다.

import sys

# n 입력
n = int(sys.stdin.readline().rstrip())

# 약수 입력
arr = list(map(int, sys.stdin.readline().split()))

# 풀이
arr.sort()  # 오름차순 정렬 수행 후
result = arr[0] * arr[len(arr) - 1]  # 가장 작은 약수와 가장 큰 약수의 곱은 N이 된다.
print(result)

# 그리디 알고리즘
# 백준 11399번
# 등급 실버 3

# 문제 해결 아이디어
# 인출하는데 소모되는 누적시간이 가장 작은 합을 구하는 문제이다.
# 시간의 최소 합은 소요시간을 작은 순서로 배열했을때 최소의 합을 얻을수 있다.
# 따라서 소요시간 리스트(q)를 오름차순을 진행하고
# 소요시간 리스트(q)에 각각의 누적시간을 대입하고
# 리스트의 총합(sum)을 구하면 된다.

import sys

n = int(input())
q = list(map(int, sys.stdin.readline().split()))

q.sort()
count = 0

for i in range(1, n):
    q[i] += q[i-1]

print(sum(q))

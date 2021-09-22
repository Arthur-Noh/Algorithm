# 그리디 알고리즘
# 백준 1783번
# 등급 실버 4

# 문제에서 중요하게 생각해야 하는 부분
# 현재 수업의 종료시간과 다음 수업의 시작시간 과의 관계

# 1) 현재 수업의 종료시간이 다음 수업의 시작시간보다 빠르면 추가 강의실 개설
# 2) 현재 수업의 종료시간이 다음 수업의 시작시간보다 느리면 이어서 수업(강의실 추가 x)

# 일반적으로 풀면 시간 초과가 발생하므로
# O(log n) 우선순위 큐를 사용해본다. 시간 복잡도는 O(n log n) 이 된다.

# 문제 해결 아이디어
# 수업을 정렬하고 종료시간(A 수업)을 시작시간(B 수업)과 비교한다.
# 만약 시작시간(B)가 종료시간(A)보다 크거나 같다면 같은 강의실에서 수업을 한다.
# 원래있던 종료시간(A)를 큐에서 삭제하고 새로운 종료시간(B)를 큐에 추가한다.

# 종료시간(A)가 시작시간(B)보다 크다면 같은 강의실에서 수업을 할 수 없다.
# 따라서 기존의 강의를 삭제하기 않고 시작강의를 새롭게 큐에 삽입하여 강의를 만든다.

import heapq
import sys

n = int(input())
q = []

for i in range(n):
    q.append(list(map(int, sys.stdin.readline().split())))
q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if q[i][0] < room[0]:
        heapq.heappush(room, q[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, q[i][1])

print(len(room))

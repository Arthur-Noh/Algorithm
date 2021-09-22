# 그리디 알고리즘
# 백준 11000번
# 등급 골드 5

# 시간초과

# 문제 해결 아이디어
# 가장 적은 강의실을 사용하여 모든 수업을 들을 수 있게 해라
# 가장 적은 강의실을 사용하기 위해서는 시작시간과 종료시간을 오름차순으로 정렬한다.
# 한 강의실에 배정된 수업의 종료시간이 새 수업의 시작시간보다 작으면 새 수업은 그 강의실에 배정될 수 없고
# 새 강의실이 필요하다.

# 변수 설명
# n : 수업의 갯수
# q : 모든 수업의 시작시간과 종료시간[Ti, Si]를 저장하는 배열
# room : 생성되는 강의실

import heapq

n = int(input())
q = []

for i in range(n):
    start, end = map(int, input().split())
    q.append([start, end])

q.sort()

room = []
heapq.heappush(room, q[0][1]) # 첫번째 수업시간을 미리 입력한다.

for i in range(1, n):
    if q[i][0] < room[0]: # 현재 수업 끝나는 시간보다 다음 수업 시작 시간이 빠르면
        heapq.heappush(room, q[i][1]) # 새로운 강의실 생성
    else: # 현재 강의실에 새로운 강의 가능
        heapq.heappop(room) # 새로운 강의 시간 변경을 위해서 pop 하고
        heapq.heappush(room, q[i][1]) # 새로운 강의 시간 push

print(len(room)) # 모든 강의실의 길이 출력

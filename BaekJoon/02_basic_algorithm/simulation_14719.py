# 기초 알고리즘 문제
# 백준 14719 빗물
# 등급 골드 5

# 문제 해결 아이디어 - 시뮬레이션
# 문제의 핵심은 가장 큰 높이와 인덱스를 찾고 왼쪽부터 탑까지, 오른쪽부터 탑까지 꾸준히 더해주면 된다.
# 쭉 더해준 후, 빗물이 고인 부분을 빼려면 각 높이의 합을 빼주면 된다.
import sys

# 최대 높이, 최대 높이 인덱스
max_h = 1
max_index = 0

h, w = map(int, sys.stdin.readline().split())
graph = list(map(int, sys.stdin.readline().split()))

# 최대 높이와 최대 높이 인덱스를 찾기
for i in range(len(graph)):
    if max_h < graph[i]:
        max_h = graph[i]
        max_index = i

total = 0
temp = 0

# 1) 왼쪽부터 높이가 있는 경우, 차례대로 더해준다.
# ex) graph[0] = 3이면
# 3 + 3 + 3 ...
for i in range(max_index + 1):
    if graph[i] > temp:
        temp = graph[i]
    total += temp

temp = 0

# 2) 오른쪽부터 높이가 있는 경우, 차례대로 더해준다.
# ex) graph[7] = 2이면
# 2 + 2 + 2 ...
for i in range(w - 1, max_index, -1):
    if graph[i] > temp:
        temp = graph[i]
    total += temp

# 총 합에서 그래프에 해당하는 값을 빼주면 빗물의 총량이 된다.
sys.stdout.write("{0}\n".format(total - sum(graph)))

# 프로그래머스
# 코딩테스트 고득점 Kit
# 스택/큐 : 다리를 지나는 트럭

# 문제 해결 아이디어
# 문제 이야기가 좀 이상한데
# 트럭이 다리를 지날때 1초에 1거리를 이동한다는 조건이 빠져있다.

# 지금까지는 deque를 잘 몰라서 사용하지 않았지만
# 스텍/큐를 사용할때는 양방향 스택 구조가 가능한 deque를 사용하는 것이
# 시간 절약에 도움이 된다.

# 다리 위 트럭 무게의 총합, 대기중인 트럭 큐, 그리고 다리 큐 (트럭이 올라갈) 을 생각하면 쉽게 해결할 수 있다.

from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_weight = 0
    waiting = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])

    while len(waiting) or bridge_weight > 0:
        remove_truck = bridge.popleft()
        bridge_weight -= remove_truck

        if len(waiting) and bridge_weight + waiting[0] <= weight:
            new_truck = waiting.popleft()
            bridge_weight += new_truck
            bridge.append(new_truck)

        else:
            bridge.append(0)

        time += 1
    return time


print(solution(bridge_length, weight, truck_weights))

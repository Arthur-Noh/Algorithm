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
    bridge_weight = 0  # 다리 위 트럭 무게의 총합
    waiting = deque(truck_weights)  # 대기중인 트럭들(무게)
    bridge = deque([0 for _ in range(bridge_length)])  # 다리 (길이만큼 q로 표현)

    while len(waiting) or bridge_weight > 0:  # 대기중인 트럭이 있거나, 다리 위가 비지 않았을 때 동안 반복
        remove_truck = bridge.popleft()  # 다리 위의 트럭 하나를 제거한다.
        bridge_weight -= remove_truck

        if len(waiting) and bridge_weight + waiting[0] <= weight:  # 대기가 있고, 다리위에 트럭을 올릴 수 있을 때
            new_truck = waiting.popleft()  # 대기 중인 트럭을 하나 꺼내서
            bridge_weight += new_truck  # 다리 위에 새 트럭 무게를 추가한다.
            bridge.append(new_truck)  # 다리에 새 트럭을 추가한다.

        else:  # 트럭을 올릴 수 없다면
            bridge.append(0)  # 0을 넣어 다리 길이를 유지한다.

        time += 1
    return time


print(solution(bridge_length, weight, truck_weights))

import collections
def sum_bridge(queue_bridge):
    sum_b = 0
    if len(queue_bridge) > 0:
        for weight, t in queue_bridge:
            sum_b = sum_b + weight
    return sum_b

def solution(bridge_length, weight, truck_weights):
    queue_wait    = collections.deque(truck_weights) # 다리 밖 대기열 큐
    queue_bridge  = collections.deque() # 다리 위 트럭 큐

    t = 0
    while len(queue_wait)>0 or len(queue_bridge)>0:
        # 다리 위에 있는 트럭들 1칸씩 이동
        for i in range(len(queue_bridge)):
            queue_bridge[i] = (queue_bridge[i][0], queue_bridge[i][1] + 1)

        # 다리 끝에 도달한 트럭은 하차
        if len(queue_bridge)>0 and queue_bridge[0][1]>bridge_length:
            queue_bridge.popleft()

        # 다리 무게 한계를 넘지 않으면 새로운 트럭이 다리 진입
        if len(queue_wait)>0 and weight - sum_bridge(queue_bridge) >= queue_wait[0]:
            truck = queue_wait.popleft()
            queue_bridge.append((truck, 1))

        t = t + 1

    answer = t
    return answer

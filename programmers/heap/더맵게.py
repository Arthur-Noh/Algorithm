# 프로그래머스
# 코딩테스트 고득점 Kit
# 힙 : 더 맵게

# 문제 해결 아이디어
# 맨처음에는 큐를 이용해서 정렬을 하는 풀이 방식을 생각했는데
# 정답은 맞을지 몰라도 속도가 참 느려졌다. 아마도 sorted를 하는 시간이 많이 소요되기 때문이다.
# 따라서 문제에서 의도한 바와 같이 heap를 사용하여 자동 정렬을 수행하면 시간이 훨씬 단축된다.

import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 6


def solution(scoville, K):
    heap = []
    count = 0

    for hot_level in scoville:  # 단순하게 이렇게 정렬을 수행할 수도 있고
        heapq.heappush(heap, hot_level)

    heapq.heapify(scoville)  # 뭐 이런식으로 간단하게 힙 으로 만들수 있다.

    while heap[0] < K:  # 가장 맨 앞 값(가장 작은 값이)이 K보다 작을동안 반복
        try:  # 힙에 다시 요소들을 빼서 힙으로 넣어준다.
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        except IndexError:
            return -1  # 불가능하면 -1을 리턴
        count += 1

    return count


print(solution(scoville, K))  # 정답 : 2

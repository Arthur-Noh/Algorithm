# 프로그래머스
# 코딩테스트 고득점 Kit
# 스택/큐 : 기능개발

# 문제 해결 아이디어
# 현재 진도율과 시간 * 속도가 100 이상일때 갯수를 세두고, 가장 앞 값을 pop 한다.
# 만약에 100보다 낮은 값을 만날때, 갯수가 1 이상이라면 지금까지 세었던 값을 정답에 넣고 다시 갯수를 0으로 초기화한다.
# 이 시간은 계속 돌아가게 만든다면 O(n) 만큼의 시간 복잡도로 해결할 수 있다.


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0

    while len(progresses) > 0:
        if progresses[0] + time * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1

    answer.append(count)

    return answer


print(solution(progresses, speeds))  # 정답 : [1, 3, 2]

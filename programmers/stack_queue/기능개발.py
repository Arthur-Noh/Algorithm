# 코딩 테스트 연습 - 프로그래머스
# 스택/큐 - 기능개발

# 기능 개선 작업을 수행중이다. 기능의 진행도가 100%가 되면 서비스에 반영할 수 있다.
# 기능의 개발속도는 모두 다르다.
# 뒤에 있는 기능이 앞의 기능보다 먼저 진행도가 100%가 될 수 있다.
# 이때 뒤 기능은 앞 기능이 배포될 때 동시에 베포 된다.

# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 : progresses
# 각 작업의 개발 속도가 적힌 정수 배열 : speeds
# 각 배포마다 몇개의 기능이 배포되는지 return 해야한다.

# 문제 해결 아이디어
#


progresses = [93, 30, 55]
speeds = [1, 30, 5]


def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    # 종료 조건
    # 큐가 빌 때까지 반복을 수행한다.
    while progresses:
        # 실행 조건
        # 가장 앞 진행도 + 시간 * 진행속도 >= 100 일때
        # 가장 앞 요소를 제거하고, 갯수를 세어준다.
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        # 실행 조건
        # 아닌 경우 시간을 1 늘려준다.
        # 만약에 갯수가 이미 세어져 있다면
        # answer에 count를 넣어주고
        # 다시 count를 0으로 초기화 해준다.
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    
    # 마지막에 모든 요소가 뽑혀 마지막 실행이 되지 않으므로 임의로 넣어준다.
    answer.append(count)

    return answer


print(solution(progresses, speeds))

# 프로그래머스
# 코딩테스트 고득점 Kit
# 스택/큐 : 프린터

# 문제 해결 아이디어
# 주어진 조건
# 1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
# 2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
# 3. 그렇지 않으면 J를 인쇄합니다.

# 중요도가 들어있는 배열이 전달되는데
# 맨 앞에 가장 높은 중요도를 가진 인자가 있다면 배출되고
# 아니라면 맨 뒤로 보낸다.
#
# 간단하게 생각해서
# 위치를 어떻게 옮길지 생각하면 된다.
# 가장 큰 값이 맨 앞에 오면 빼버리고, 위치를 하나 뺀다.
# 가장 큰 값이 아니라면 맨 뒤로 보내고, 위치를 하나 뺀다.
# 내 값이 가장 맨 앞으로 왔는데, 가장 큰 값이 아니라면, 맨 뒤로 보내고, 위치를 맨뒤로 한다.
# 내 값이 가장 맨 앞으로 왔는데, 가장 큰 값이라면, 몇번째인지 갯수 세고 탈출한다.


priorities = [2, 1, 3, 2]
location = 2


def solution(priorities, location):
    count = 0

    while len(priorities) != 0:  # 배열의 길이가 0이 되지 않을 때 까지 반복한다.
        if location == 0:  # 내가 지정한 prioritie가 맨 앞에 온다면
            if priorities[0] < max(priorities):  # 내가 지정한 prioritie가 최댓값이 아니면 맨 뒤로 보내기
                priorities.append(priorities.pop(0))
                location = len(priorities) - 1
            else: # 내가 지정한 prioritie가 현재 배열에서 가장 큰 값이라면
                count += 1
                break # 탈출
        else:  # 위치가 맨 앞이 아니고 다른 인자가 맨 앞이라면
            if priorities[0] < max(priorities):  # 최댓값이 아니면 맨 뒤로 보내기
                priorities.append(priorities.pop(0))
                location -= 1
            else:  # 가장 큰 값이 앞에 오면
                count += 1
                priorities.pop(0)
                location -= 1

    return count


print(solution(priorities, location))  # 정답 : 1

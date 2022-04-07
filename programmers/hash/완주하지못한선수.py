# 프로그래머스
# 코딩테스트 고득점 Kit
# 해시 : 완주하지 못한 선수

# 문제 해결 아이디어
# 내 기준의 가독성을 높이기 위해 zip 함수를 사용하였다.
# 두 배열의 정렬을 수행한다.
# 각각의 참여자와 완주자 명단을 하나씩 받아서
# 같은 경우에는 넘어가고 다른 경우에는 그 참여자는 완주하지 못했으므로 즉시 리턴한다.
# 만약에 모두 같았다면, 가장 마지막에 위치한 참여자는 완주하지 못했으므로 배열의 마지막 값을 리턴한다.

def solution(participant, completion):

    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant[-1]


participant = ["leo", "kiki", "eden"]
completion = ["kiki", "eden"]

print(solution(participant, completion))

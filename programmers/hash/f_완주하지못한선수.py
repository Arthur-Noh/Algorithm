# 코딩 테스트 연습 - 프로그래머스
# 해시 - 완주하지 못한 선수
# 실패 - 시간초과

# 문제 해결 아이디어
# 단순하게 처음부터 쭉 반복하여 없는 이름을 찾는다.
# 중복된 이름이 있을때마다 이름을 제거한다.
# 중복된 이름이 없으면 저장하고 바로 출력하지만, 중복된 이름이 없다면 코드가 끝까지 실행된 후
# 마지막 남은 리스트를 출력한다.

participant = ['miskav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']


def solution(participant, completion):
    answer = ''
    p = participant
    c = completion

    for name in c:
        if name in p:
            p.remove(name)
        else:
            answer = name

    if len(answer) == 0:
        answer = p[0]

    return answer

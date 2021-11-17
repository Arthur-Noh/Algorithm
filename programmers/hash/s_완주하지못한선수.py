# 코딩 테스트 연습 - 프로그래머스
# 해시 - 완주하지 못한 선수
# 성공

# 문제 해결 아이디어
# 이전의 풀이는 코드는 맞았지만, 효율성(시간)에서 틀렸다.
# 효율적은 방법을 찾아본 결과 collections가 가장 좋았지만
# 배열을 같은 인덱스끼리 짝을 지어주는 zip 함수를 사용하였다.

# zip 함수
# 배열을 같은 인덱스 번호끼리 짝을 짓는다.
# 배열의 길이가 다를 경우 같은 인덱스 번호끼리만 짝을 지어주고 나머지는 제외한다.

# 먼저 두 배열의 정렬을 수행한다.
# for p, c in zip(p, c)를 통해 각각의 p와 c를 입력받고
# 그 둘의 값이 다를때 리턴을 수행한다.
# 만약에 리턴이 수행되지 않으면
# 한명이 남았다는 소리이므로 마지막 인원을 리턴시켜준다.

participant = ['miskav', 'stanko', 'mislav', 'ana']
completion = ['stanko', 'ana', 'mislav']


def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant[-1]


print(solution(participant, completion))

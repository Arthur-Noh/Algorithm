# 코딩 테스트 준비 - 기초
# 백준 1759 암호 만들기
# 등급 골드 5

# 문제 해결 아이디어
# 백트래킹으로 해결할 수 있다.
# 먼저 단어들을 입력을 받고, 방문을 기록할 리스트를 생성한다.
# 그리고 단어들을 오름차순으로 정렬한다.
# dfs 에서는 최종 문자의 길이가 되었을 때 자음과 모음의 갯수를 세어 조건에 충족한다면 출력한다.
# 아닌 경우는 그냥 안하기 때문에 생각할 필요가 없다.
# 중복을 허용하지 않기 때문에 시작 값을 dfs의 값으로 넘겨주면 된다.

import sys

l, c = map(int, sys.stdin.readline().split())
words = list(map(str, sys.stdin.readline().split()))
visited = [False] * c
s = []

words.sort()


def dfs(start):
    if len(s) == l:  # 만약 단어들을 저장한 리스트의 길이가 l과 같다면
        vow = 0  # 모음
        con = 0  # 자음

        for i in range(l):  # 자음과 모음의 갯수를 세서
            if s[i] in 'aeiou':
                vow += 1
            else:
                con += 1
        if vow >= 1 and con >= 2:  # 조건에 충족한다면 출력하고 리턴
            print(''.join(map(str, s)))
            return
        else:
            return

    for i in range(start, c):  # 만약 단어의 수가 더 부족하다면
        if not visited[i]:  # 방문하지 않았다면
            visited[i] = True  # 방문 처리를 하고
            s.append(words[i])  # 단어를 추가시켜 준다.
            dfs(i + 1)  # 그리고 다음 dfs를 수행하게 값을 하나 증가시켜 넘겨준다. / 중복을 허용하지 않기 때문에
            visited[i] = False  # 다시 온다면 비방문 처리를 하고
            s.pop()  # 단어를 빼어낸다.


dfs(0)

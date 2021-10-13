# 기초 알고리즘 문제
# 백준 14719 빗물
# 등급 골드 4

# 문제 해결 아이디어 - DFS
# 모든 단어가 anta 로 시작해서 tica 로 끝나므로
# a c i n t 는 반드시 포함되어 있어야 한다.
# 따라서 가르치는 단어의 갯수 k 가 5보다 작다면 표현 가능한 단어의 갯수는 0개이다.
# dfs를 사용하여 완전 탐색을 수행하면 된다.

import sys
n, k = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().rstrip()[4:-4] for _ in range(n)]  # 쓸데없는 반복을 막기 위해

answer = 0
learn = [0] * 26

for i in ('a', 'c', 'i', 'n', 't'):  # 무조껀 배워야 하는 단어
    learn[ord(i) - ord('a')] = 1


def dfs(index, count):
    global answer

    if count == k - 5:
        readcnt = 0
        for word in words:  # 단어 리스트의 단어를 꺼나서
            check = True
            for w in word:  # 단어의 한글자 씩 비교해 가면서
                if not learn[ord(w) - ord('a')]:  # 배우지 않았을 경우
                    check = False  # 즉시 탈출
                    break
            if check:
                readcnt += 1

        answer = max(answer, readcnt)
        return

    for i in range(index, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, count + 1)
            learn[i] = False


dfs(0, 0)
sys.stdout.write("{0}\n".format(answer))

# 코딩 테스트 준비 - 기초
# 백준 15649 N 과 M(1)
# 등급 실버 3

# 문제 해결 아이디어
# 이 문제는 DFS의 일종인 백 트래킹으로 해결할 수 있다.
# 백트래킹 (퇴각 검색)
# - 길을 가다가 이 길이 아닌 것 같으면 왔던 길로 되돌아가 다른 경로로 진행
# - 보통 재귀로 구현하며 조건이 맞지 않으면 종료한다.
# - DFS(깊이 우선 탐색) 기반
# 참고 : https://jiwon-coding.tistory.com/34


import sys
n, m = map(int, sys.stdin.readline().split())

s = []  # m 개의 수열을 저장하기 위한 리스트


def dfs():
    if len(s) == m:  # 리스트에 들어간 수열의 갯수가 m 개가 되면 숫자들을 모두 출력하고 탈출
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        if i not in s:  # 중복 숫자가 배열에 있는지 확인하고
            s.append(i)  # 없다면 리스트에 넣어주고
            dfs()  # 다시 dfs를 수행한다.
            s.pop()


dfs()

# 코딩 테스트 준비 - 기초
# 백준 2529 부등호
# 등급 실버 2

# 문제 해결 아이디어
# 부등호를 만족시키면서 최솟값과 최댓값을 출력하라는 문제이다.
# 백트래킹 방식으로 문제를 해결했다.
# 부등호 갯수가 n 개라면 n + 1개의 숫자를 고르는 문제이다.

import sys
n = int(sys.stdin.readline().rstrip())
sign = list(sys.stdin.readline().split())
max_value = ''
min_value = ''
visited = [False] * 10


# 입력된 부등호에 따라 True 와 False 를 반환해준다.
def possible(x, y, symbol):
    if symbol == '<':
        return x < y
    if symbol == '>':
        return x > y


# dfs 의 인자 값으로 인덱스 번호와 문자열(숫자)를 받는다.
def dfs(idx, s):
    global max_value
    global min_value

    # 종료 조건 : 만약 인덱스 번호가 n + 1 이라면(n + 1)개의 숫자를 골랐다면
    if idx == n + 1:
        # 최솟값의 경우 : 처음 성립한 조합이 최솟값이 된다.
        # 따라서 가장 먼저 통과한 조합은 바로 min_value 에 넣어주고
        # 그 다음 통과하는 조합이 max_value 가 된다.
        if not len(min_value):
            min_value = s
        else:
            max_value = s
        return
    
    # 실행 조건
    for i in range(10):
        if visited[i]:  # 방문을 한 경우 다시 방문하지 않음
            continue
        
        # 인덱스 번호가 0 (첫번째 실행) 이거나
        # 부등호가 가능한지를 넘겨주었을 때 가능하다면
        # 같은 숫자는 앞선 continue 로 인해 반복하지 않음
        if idx == 0 or possible(s[-1], str(i), sign[idx - 1]):
            visited[i] = True
            dfs(idx + 1, s + str(i))
            visited[i] = False


dfs(0, '')
print(max_value)
print(min_value)

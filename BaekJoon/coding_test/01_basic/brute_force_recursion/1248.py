# 코딩 테스트 준비 - 기초
# 백준 1248 맞춰봐
# 등급 골드 3

# 문제 해결 아이디어
# 백트래킹으로 해결할 수 있다.
# 수열의 크기 N 이 주어진다. (N <= 10)
# N(N+1)/2 길이의 문자열이 주어진다.
# 처음 N개의 문자는 부호 배열의 첫번째 줄에 해당하고
# 다음 N-1개의 문자는 두번째 줄에 해당한다.
# 마지막 문자는 N 번째 줄에 해당하는 문자이다.
# 참고 : https://hazung.tistory.com/127

# 예시
# 4
# -+0++++--+

# 출력
# -2 5 -3 1

# A = [-2, 5, -3, 1] 일 댸
# 부호의 뜻은
# 첫번째 줄 : A[0], A[0] + A[1], A[0] + A[1] + A[2], A[0] + A[1] + A[2] + A[3]
# 두번째 줄 : A[1], A[1] + A[2], A[1] + A[2] + A[3]
# 세번째 줄 : A[2], A[2] + A[3]
# 네번째 줄 : A[3]
# 으로 합의 부호를 나타낸 것이다.

# 행렬을 한번 그려보면 다음과 같다.
#   0  1  2  3
# 0 -  +  0  +
# 1    +  +  +
# 2       -  -
# 3          +
# 여기서 S[0][0], S[1][1], S[2][2], S[3][3]은 -2, 5, -3, 1의 부호와 일치한다.
# 이것을 이용하여 탐색 시간을 줄일 수 있다.
# S[index][index]가 '+'인 경우 1 ~ 10 탐색, '-'인 경우 -10 ~ -1 을 탐색한다.

#  -2  5 -3  1
#   0  1  2  3
# 0 -  +  0  + -> 1 + (-3) + 5 + (-2)
# 1    +  +  + -> 1 + (-3) + 5
# 2       -  - -> 1 + (-3)
# 3          + -> 1
# S 에 있는 부호들의 의미는 A의 인덱스3의 합, 인덱스 3 2의 합, 인덱스 3 2 1의 합, 인덱스 3 2 1 0의 합의 부호이다.
# 인덱스 N이 만족해야 하는 조건이다.
# 알아낸 규칙을 바탕으로 함수를 작성한다.
# solve 함수는 S 대각선 값이 0일때와 0이 아닐때로 나눠서 생각한다.
# S[index][index]가 0이라면, 배열의 index 값이 0이라는 뜻이니 0을 넣고 다음 인덱스의 함수를 부른다.
# S[index][index]가 0이 아니라면, 양음에 따라 1 ~ 10, -10 ~ -1 범위의 숫자를 조사한다.
# check 함수로 S의 부호들이 맞는 값인지 확인한다.

import sys
n = int(sys.stdin.readline().rstrip())
arr = list(sys.stdin.readline().rstrip())
s = [[0] * n for _ in range(n)]

# ex)
#   0  1  2  3
# 0 -  +  0  +
# 1    +  +  +
# 2       -  -
# 3          +
for i in range(n):
    for j in range(i, n):
        temp = arr.pop(0)
        if temp == '+':
            s[i][j] = 1
        elif temp == '-':
            s[i][j] = -1

result = [0] * n


# 부호와 합이 일치하는지 확인하는 함수
def check(idx):
    sum_ = 0
    # 인덱스의 마지막 부호부터 순차적으로 계산을 진행한다.
    for i in range(idx, -1, -1):
        sum_ += result[i]
        if sum_ == 0 and s[i][idx] != 0:
            return False
        elif sum_ < 0 and s[i][idx] >= 0:
            return False
        elif sum_ > 0 and s[i][idx] <= 0:
            return False
    return True


def dfs(idx):
    # 종료조건 : 문제 없이 n 번 반복을 하면 True 반환
    if idx == n:
        return True

    # 실행조건 : 대각선 값이 0 이라면 그대로 0을 대입
    if s[idx][idx] == 0:
        result[idx] = 0
        dfs(idx + 1)

    # 실행조건 : 1 ~ 10까지 하나씩 곱하여 결과 값에 넣어본다.
    # 넣었을 때 값이 성립하면서 다음 dfs 값도 성립을 하면 True 반환
    for i in range(1, 11):
        result[idx] = s[idx][idx] * i
        if check(idx) and dfs(idx + 1):
            return True

    return False


dfs(0)
print(' '.join(map(str, result)))

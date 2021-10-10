# 기초 수학 문제
# 백준 14888 연산자 끼워넣기
# 등급 실버 1

# 문제 해결 아이디어
# 이 문제는 DFS 로 풀 수 있다.
# 차례대로 입력 받은 후
# 해당 연산자에 해당하는 경우 깊이 탐색 알고리즘을 수행하도록 코드르 작성하면 된다.
import sys

# 수의 개수 N
n = int(sys.stdin.readline().rstrip())

# 수 입력 받기
arr = list(map(int, sys.stdin.readline().split()))

# 연산자의 갯수 입력
o = list(map(int, sys.stdin.readline().split()))

# 최대, 최솟값
MAX_SIZE = -1000000001
MIN_SIZE = 1000000001


# DFS
# 횟수, 다음 값, 덧셈, 뺄셈, 곱셈, 나눗셈 
# 순서로 입력을 받아서 재귀함수로 처리하면 된다.
# 그러면서 최종 횟수에 다다랐을때 전역변수에 최댓값과 최솟값을 비교하여 저장하면 된다.
def dfs(count, result, p, m, mul, div):
    global MAX_SIZE
    global MIN_SIZE

    if count == n:
        MAX_SIZE = max(MAX_SIZE, result)
        MIN_SIZE = min(MIN_SIZE, result)
        return

    if p:
        dfs(count + 1, result + arr[count], p - 1, m, mul, div)
    if m:
        dfs(count + 1, result - arr[count], p, m - 1, mul, div)
    if mul:
        dfs(count + 1, result * arr[count], p, m, mul - 1, div)
    if div:
        dfs(count + 1, -(-result // arr[count]) if result < 0 else result // arr[count], p, m, mul, div - 1)


# 연산자의 갯수가 수의 갯수보다 1개 작기 때문에 1로 시작한다. 
dfs(1, arr[0], o[0], o[1], o[2], o[3])

sys.stdout.write("{0}\n{1}\n".format(MAX_SIZE, MIN_SIZE))

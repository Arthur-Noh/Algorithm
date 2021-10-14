# 코딩 테스트 준비 - 기초
# 백준 16936번 나3곱2
# 등급 골드 5

# 문제 해결 아이디어
# 이 문제는 서로소의 특징으로 해결할 수도 있고, 일반적 dfs로 해결할 수 있다.
# 나는 dfs 로 해결하였다.
# DFS 에서 
# DFS의 인자로 i 번째에 해당하는 값을 첫번째 인자로 취급하고 반복 연산을 수행하도록 한다.
# i 번째 해당하는 인자가 처음 값이니 제거를 하고, 정렬될 배열 A 에 저장을 한다.
# 그 다음부터 문제에서 주어진 연산을 수행한다.
# 
# 만약 2로 곱해진 원소가 기존 리스트에 존재하면 -> 두배 곱한 값으로 dfs 다시 수행
# 만약 3으로 나눠 떨어지고, 그 나눈 값이 기존 리스트에 존재하면 -> 3으로 나눈 몫으로 다시 dfs 수행
# 종료 지점을 설정해야 하니까 만약 더이상 값을 못찾으면 false를 리턴하고
# 만약 배열이 텅 비었다면 그것은 정답이니까 True를 반환한다.
#
# 여러번 시작값을 바꿔가면서 반복하여 flag 값이 True가 되는 순간이 바로 정답인 순간이다.

import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))


# DFS
def dfs(x, arr, A):
    arr.remove(x)
    A.append(x)
    least_one = False

    if not arr:
        return True

    if x * 2 in arr:
        least_one = True
        return dfs(x * 2, arr, A)

    if x % 3 == 0 and x // 3 in arr:
        least_one = True
        return dfs(x // 3, arr, A)

    if not least_one:
        return False


for i in range(n):
    A = []
    flag = dfs(arr[i], arr.copy(), A)
    if flag:
        print(A)
        break

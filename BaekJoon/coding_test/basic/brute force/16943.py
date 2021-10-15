# 코딩 테스트 준비 - 기초
# 백준 16943 숫자 재배치
# 등급 실버 1

# 문제 해결 아이디어
#

import sys

# 두 정수 A, B 입력
a, b = sys.stdin.readline().split()

# 두 정수를 각각 list로 저장해준다.
a = list(map(int, a.strip()))
b = list(map(int, b.strip()))

result = -1  # 결과를 입력받을 값

length = len(a)
check = [False] * length


# DFS
def dfs(idx, cur_num):
    global result

    if idx == length:
        if int(cur_num) <= int(''.join(map(str, b))):
            result = max(result, int(cur_num))
        return

    for i in range(length):
        if idx == 0 and a[i] == 0:
            continue

        if not check[i]:
            check[i] = True
            dfs(idx + 1, cur_num + str(a[i]))
            check[i] = False


dfs(0, '')

print(result)

# 코딩 테스트 준비 - 기초
# 백준 10974 모든 순열
# 등급 실버 3

# 문제 해결 아이디어
# next permutation 알고리즘을 사용하면 된다.
# 사전순으로 정렬한 배열 A 가 있다면
# A[i] < A[i + 1]이 되는 i 값을 찾고 - x
# 찾은 x 다음 지점부터(x + 1), 끝까지 비교하면서
# A[x] < A[i] 가 되는 i 지점을 찾는다. - y
# 그 찾은 A[x], A[y]를 서로 스왑하고
# A[:x + 1] 지점 까지는 그대로 A[x + 1:] 끝까지는 오름차순 정렬을 수행한 뒤 값을 전달하면 된다.


import sys
n = int(sys.stdin.readline().rstrip())
s = list(i for i in range(1, n + 1))


def find(bs):
    x = -1

    # 1. x 의 최댓값 구하기
    for i in range(len(bs) - 1):
        if bs[i] < bs[i + 1]:
            x = i

    # 마지막
    if x == -1:
        return -1

    # 2. y 의 최댓값 구하기
    for i in range(x + 1, len(bs)):
        if bs[x] < bs[i]:
            y = i

    # 3. x 와 y 바꾸기
    bs[x], bs[y] = bs[y], bs[x]

    # 4. k 이후 오름차순으로 정렬하기
    return bs[:x + 1] + sorted(bs[x + 1:])


def print_arr(s):
    for num in s:
        sys.stdout.write('{0} '.format(num))
    sys.stdout.write('\n')


while True:
    print_arr(s)
    s = find(s)

    if s == -1:
        break

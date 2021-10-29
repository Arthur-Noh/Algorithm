# 코딩 테스트 준비 - 기초
# 백준 11723 집합
# 등급 실버 5

# 문제 해결 아이디어
# 비트마스크를 사용하여 푸는 문제이다.
# 참고 : https://hooongs.tistory.com/208

import sys
m = int(sys.stdin.readline().rstrip())
bit = 0

for i in range(m):
    command = sys.stdin.readline().split()

    if command[0] == 'all':
        bit = (1 << 20) - 1
    elif command[0] == 'empty':
        bit = 0
    else:
        op = command[0]
        num = int(command[1]) - 1

        # add
        if op == 'add':
            bit |= (1 << num)

        # remove
        elif op == 'remove':
            bit &= ~(1 << num)

        # check
        elif op == 'check':
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)

        # toggle
        elif op == 'toggle':
            bit = bit ^ (1 << num)

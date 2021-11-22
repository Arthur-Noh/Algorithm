# 코딩 테스트 준비 - 기초
# 백준 10866 덱
# 등급 실버 4

# 문제 해결 아이디어
# 간단한 덱큐 구현 문제이다.
# 덱큐 함수 쓸줄 알면 쉽게 해결할 수 있다.

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
dq = deque()

for _ in range(n):
    command = sys.stdin.readline().rstrip()

    if command.startswith('push_front'):
        c = command[11:]
        dq.appendleft(int(c))

    elif command.startswith('push_back'):
        c = command[10:]
        dq.append(int(c))

    elif command.startswith('pop_front'):
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())

    elif command.startswith('pop_back'):
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())

    elif command.startswith('size'):
        print(len(dq))

    elif command.startswith('empty'):
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif command.startswith('front'):
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])

    elif command.startswith('back'):
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])

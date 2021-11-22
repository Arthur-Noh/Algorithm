# 코딩 테스트 준비 - 기초
# 백준 10845 큐
# 등급 실버 4

# 문제 해결 아이디어
# 기초적인 큐 구현 문제
# 생각할 점이라면 왼쪽에서 오른쪽으로 채우는 형식으로 구현한다.
# insert 를 사용하여 list의 가장 앞 부분에 계속 새로운 수를 채우고
# pop를 통해서 맨 뒷자리 수(가장 먼저들어온 수)를 빼내는 형식으로 구현하면 된다.

import sys
n = int(sys.stdin.readline().rstrip())
queue = []

for _ in range(n):
    command = sys.stdin.readline().rstrip()

    if command.startswith('push'):
        c = command[5:]
        queue.insert(0, int(c))

    elif command.startswith('pop'):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())

    elif command.startswith('size'):
        print(len(queue))

    elif command.startswith('empty'):
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif command.startswith('front'):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

    elif command.startswith('back'):
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

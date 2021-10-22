# 코딩 테스트 준비 - 기초
# 백준 6064 카잉 달력
# 등급 실버 1

# 문제 해결 아이디어
# 참고 : https://pacific-ocean.tistory.com/126
# 그냥 1씩 더하는 풀이는 시간 초과가 난다.
# 정답을 K 번째 해 라고 하자
# K - x 에 M 을 나누면 나머지가 0이다.
# 마찬가지로 K - y 에 N 을 나누면 나머지는 0이다.
# 정답 K는 x 나 y에 M과 N을 계속 더한 값 중 하나이다.
# x 에 M을 계속 더해주고 y를 뺀 값에 N이 나누어 떨어진다면 그 값이 정답이다.
import sys


def kaing(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0:
            return x
        x += m
    return -1


t = int(sys.stdin.readline().rstrip())
for i in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    print(kaing(m, n, x, y))

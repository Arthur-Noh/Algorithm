# 코딩 테스트 준비 - 기초
# 백준 16922 로마 숫자 만들기
# 등급 실버 3

# 문제 해결 아이디어
# 각 순서에 대해서 4개가 들어갈 수 있다.
# 순서가 중요하지 않으니까 각각 몇개가 들어가는지 고려하면 된다.
# 마지막 문자는 앞에 3개로 정해진 값에서 빼기 연산하여 정한다.
import sys
n = int(sys.stdin.readline().rstrip())
s = []

for i in range(n + 1):
    for j in range(n + 1 - i):
        for k in range(n + 1 - i - j):
            t = n - i - j - k
            total = i * 1 + j * 5 + k * 10 + t * 50
            s.append(total)

print(len(set(s)))

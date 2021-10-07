# 기초 수학 문제
# 백준 2501번 약수 구하기
# 등급 브론즈 3

# 문제 해결 아이디어
# 입력된 N을 나누어 0으로 떨어지는 약수들을 리스트에 저장한다.
# 약수들이 저장된 리스트에서 K 번째에 해당하는 값을 출력한다.

import sys

# N, K 입력
n, k = map(int, sys.stdin.readline().split())

# N의 약수를 저장할 리스트
m = []

# N의 약수를 구하기
for i in range(1, n + 1):
    if n % i == 0: # N을 i로 나눈 나머지가 0이라면
        m.append(i)

# K 번째에 해당하는 값 출력하기
if k > len(m): # 만약 K 보다 약수의 갯수m 의 길이가 짧다면 0을 출력
    sys.stdout.write("0\n")

else:
    sys.stdout.write("{0}\n".format(m[k - 1]))

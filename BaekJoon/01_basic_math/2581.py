# 기초 수학 문제
# 백준 2581 소수
# 등급 실버 5

# 문제 해결 아이디어
# 소수 찾는 알고리즘을 사용하면 된다.
# 1 ~ n-1 까지 나눠서 0이 되는 자연수가 있을 경우 소수가 아니므로 제외
# 소수인 경우 소수 리스트에 저장
# 소수 리스트의 길이가 0인 경우(비어있는 경우) -1  출력

# 계속 소수가 아니라는 것이 밝혀졌는데 반복문을 돌리게 되면
# 시간을 초과할 수 있기 때문에 break로 탈출 한다.

import sys

# M, N 입력
m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
sosu = [] # 소수를 저장할 리스트

for number in range(m, n + 1):
    error = 0  # 소수를 찾는 변수

    if number > 1:  # 수가 1보다 클 때
        for i in range(2, number):  # 2부터 n - 1까지 나누었을 때
            if number % i == 0:  # 나머지가 0 인 경우
                error = 1  # 소수가 아니다
                break # 계속 쓸데없이 반복되므로 break를 써서 포문을 탈출하면 된다.

        if error == 0:  # 소수를 찾는 변수가 0이라면
            sosu.append(number)

if len(sosu) == 0: # 리스트가 비어있는 경우
    sys.stdout.write("-1\n")
else:
    sys.stdout.write("{0}\n".format(sum(sosu)))
    sys.stdout.write("{0}\n".format(sosu[0])) # 당연히 순차적으로 입력되었으므로, 첫째값이 최솟값

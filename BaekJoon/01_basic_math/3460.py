# 기초 수학 문제
# 백준 3460 이진수
# 등급 브론즈 3

# 문제 해결 아이디어
# 입력받은 양의 정수 N에 대하여 2로 나눈 나머지가 1이라면 바로 count 출력한다.
# 양의 정수 N에는 N을 2로 나눈 몫을 저장한다.


# 처음에는 이 문제를 틀렸는데
# 하나 입력 받고 바로 결과 출력하는 줄 모르고
# 한번에 다 입력받고 출력하는 줄 알았던 것이다.

# 다른사람의 풀이를 보니까 파이썬에는 정수를 이진수 문자열로 변환하는 함수(bin)이 있다고한다.
# 맨 뒤 값부터 시작해서 '1'이라는 문자가 발견될 때마다 i를 출력하는 형식을 취하면 더 쉽게 해결할 수 있다.


import sys

# 테스트 케이스의 갯수 t
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    count = 0
    temp = 0

    while n:
        if n % 2 == 1:
            sys.stdout.write("{0} ".format(count))

        n = n // 2
        count += 1

    sys.stdout.write("\n")

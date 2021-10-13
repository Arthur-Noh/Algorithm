# 코딩 테스트 준비 - 기초
# 백준 16968 차량 번호판 1
# 등급 브론즈 4

# 문제 해결 아이디어
# 수학 문제이다.
# d d 이렇게 반복되는 경우 일치하는 경우의 수를 빼고 곱해주면 된다.
# 10 * 9
# c c 이렇게 나오면 26 * 25 * 24 ... 이런 식으로 곱해주면된다.

import sys

nums = {'c': 26, 'd': 10}  # 키 벨류를 사용해서 풀이하면 쉽다.
s = sys.stdin.readline().rstrip()
answer = nums[s[0]]  # 첫번째 값을 미리 입력 한다.

for i in range(1, len(s)):
    mul = nums[s[i]]  # 곱해줄 값 준비

    if s[i] == s[i - 1]:  # 이전과 동일한 문자라면
        mul -= 1

    answer *= mul

print(answer)

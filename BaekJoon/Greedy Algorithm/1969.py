# 그리디 알고리즘
# 백준 1969번
# 등급 실버 5

# 문제 해결 아이디어
# 가장 많이 입력된 문자를 찾아서 순서대로 출력하고, 그 출력된 문자열과 입력된 문자열 사이의 다른 단어들의
# 갯수를 세 출력하는 것이다.

# 원리는 간단하게 문자열을 전부 입력받고
# 1) 문자열의 각 자리수를 검사하여 가장 많이 출력된 알파벳을 result에 저장한다.
# 2) 저장된 문자열과 입력받은 문자열들을 비교하여 다른 종류의 알파벳을 찾을때 마다 count++을 진행한다.

import sys

n, m = map(int, sys.stdin.readline().split())
DNA = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

result = ""
count = 0

for i in range(m):
    abc = [0 for _ in range(26)] # 알파벳이 26자이므로 26개의 리스트를 만들고

    for j in range(n): # 거꾸로 열부터 검사를 시작한다.
        abc[ord(DNA[j][i]) - 65] += 1 # 대문자 A의 아스키 코드 값이 65이므로 이 값을 빼주고 넣어주면 된다.

    result += chr(abc.index(max(abc)) + 65) # 가장 많은 빈도로 출력된 문자를 저장

for i in range(n): # 저장된 문자열과 입력받은 문자열 사이의 다른 종류의 알파벳을 찾을때마다 +1
    for j in range(m):
        if DNA[i][j] != result[j]:
            count += 1

print(result)
print(count)

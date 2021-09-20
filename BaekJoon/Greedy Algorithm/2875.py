# 그리디 알고리즘
# 백준 2875번
# 등급 브론즈 3

# 여학생의 수 N, 남학생의 수 M
# 인턴쉽에 참여해야하는 인원 K
n, m, k = map(int, input().split())

count = 0

# 여자 2명 이상, 남자 1명 이상
# 인턴쉽 참여 인원보다 한팀 더 만들 수 있는 상황 일 때
while n >= 2 and m >= 1 and n + m >= k + 3:
    n -= 2
    m -= 1
    count += 1

print(count)

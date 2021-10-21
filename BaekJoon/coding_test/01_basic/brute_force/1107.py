# 코딩 테스트 준비 - 기초
# 백준 1107 리모컨
# 등급 골드 5

# 문제 해결 아이디어
# 좀 지저분한 문제

# 희망 채널
n = int(input())

# 고장난 버튼 수
m = int(input())

# 0 ~ 9 까지 버튼을 가진 리모컨
remote = {str(_) for _ in range(10)}

# 고장난 버튼을 리모컨에서 제거
if m > 0:
    remote -= set(map(str, input().split()))

# 현재 보고 있는 채널
current = 100

# 현재 보고 있는 채널에서 보려는 채널까지 +- 버튼을 통해 이동해야 했을때 버튼을 눌러야하는 횟수
min_cnt = abs(current - n)

# 100만 채널까지 순회
for channel in range(1000000):
    # 현재 순회중인 채널의 각 자릿수 순회
    for number in range(len(str(channel))):
        # 현재 자릿수가 누를수 없는 버튼이라면 해당 채널은 패스
        if str(channel)[number] not in remote:
            break

        # 마지막 자릿수까지 모두 사용가능한 버튼이라면
        elif len(str(channel)) - 1 == number:
            # 채널번호 누른 횟수 len(str(channel)))와
            # 채널번호에서 희망채널까지 +-를 눌러야 하는 횟수를 더해서
            # 이전에 구한 최저횟수보다 적다면 최저횟수로 지정한다.
            min_cnt = min(min_cnt, len(str(channel)) + abs(channel - n))

print(min_cnt)

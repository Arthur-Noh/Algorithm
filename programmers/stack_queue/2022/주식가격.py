# 프로그래머스
# 코딩테스트 고득점 Kit
# 스택/큐 : 주식가격

# 문제 해결 아이디어
# 문제의 설명이 어려운데, 임의로 해석해보면
# 3원에서 2원으로 내려가는데 1초의 시간이 걸린다면,
# 3원이 1초간 유지된 것으로 간주하고 상승 시간은 1초로 간주한다.

# 큐로 생각하니까 쉽게 풀린다.
# 맨 앞 주식을 빼내서 다음 값들과 순차적으로 비교하고
# 높다면, 문제에서 요구한 1초 상승처럼 1을 더하고 탈출하고
# 낮다면, 계속 1을 추가한다.
# 반복을 마무리하면 세었던 시간을 상승 시간 리스트에 넣는다.

from collections import deque

prices = [1, 2, 3, 2, 3]


def solution(prices):
    stocks = deque(prices)
    up_time_list = []

    while len(stocks) != 0:  # 주식 큐가 비어있지 않은 동안 반복
        start_stock = stocks.popleft()  # 비교할 주식 하나를 빼낸다.
        time = 0  # 상승 시간

        for stock in stocks:  # 나머지 주식 가격을 하나씩 꺼내면서
            if start_stock > stock:  # 시작한 가격이 더 높다면
                time += 1  # 지속된 시간 1초를 추가하고 탈출
                break
            else:  # 시작한 가격이 낮다면 시간만 추가
                time += 1

        up_time_list.append(time)

    return up_time_list


print(solution(prices))

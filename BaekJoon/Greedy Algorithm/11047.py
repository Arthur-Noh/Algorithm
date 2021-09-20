# 그리디 알고리즘
# 백준 11047번

# 동전의 종류(N)과 가치의 합(K) 입력
n, k = map(int, input().split())

# 동전의 종류들 입력
coins = []
for coin in range(n):
    coins.append(input())

# 오름차순으로 입력되기 때문에 순서를 뒤집기
coins.reverse()

# 동전으로 나눠주기
count = 0

for coin in coins:
    count += k // int(coin)
    k %= int(coin)

# K 원을 만드는 데 필요한 동전의 최소 갯수
print(count)

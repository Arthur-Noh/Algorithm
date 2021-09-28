# 그리디 알고리즘
# 백준 1700번
# 등급 골드 1

# 문제 해결 아이디어
# 플러그를 빼는 횟수를 최소로 하는 프로그램을 작성하기

# 1) 만약에 다음에 사용할 전기용품이 현재 플러그에 꼽혀있는 경우 continue
# 2) 만약에 현재 플러그가 꽉 차있지 않은 경우 새로 꼽고 continue
# 3) 만약에 플러그에 모든 전기용품이 꽂혀있는 경우
# 현재 플러그의 위치부터 마지막까지 가져온 후, 다음 전기용품들을 비교하여
# 현재 플러그 안에 있는 값이 있다면
# 그 전기용품의 인덱스 값을 가져오고, 없다면 전기용품의 최대값 100+1 인 101을 입력한다.
# 전기용품들의 인덱스 값을 비교하여 가장 멀리 순서가 있는 전기용품을 가장 먼저 뽑고(없는 경우 101인 전기용품을 뽑기)
# 새로운 전기용품을 꼽으면 된다.


import sys

# n : 멀티탭의 구멍 갯수
# k : 전기용품의 총 사용횟수
n, k = map(int, sys.stdin.readline().split())

# 전기용품의 이름
name = list(map(int, sys.stdin.readline().split()))

nowPlug = []
count = 0

for i in range(k):
    # 새로 꼽을 전기용품이 플러그에 꼽혀있으면 pass
    if name[i] in nowPlug:
        continue

    # 플러그가 비어 있으면 꼽기
    if len(nowPlug) < n:
        nowPlug.append(name[i])
        continue

    # 현재 플러그의 갯수만큼의 가상의 플러그를 만들어
    # 다음에 꽂을 전기용품이 있다면 그 전기용품의 인덱스 값을 집어넣고
    # 없는 경우에는 최대값(101)을 저장하여 가장 먼저 뽑도록 한다.
    nextPlugs =[]
    hasPlug = True

    for j in range(n):
        # 현재 멀티탭 안에 다음에 꽂을 동일한 전기용품 값이 있다면
        if nowPlug[j] in name[i:]:
            # 그 전기용품의 위치를 가져오기
            name_idx = name[i:].index(nowPlug[j])
        else:
            name_idx = 101
            hasPlug = False

        # 다음에 꼽을 전기용품의 인덱스에 값을 넣어주기
        nextPlugs.append(name_idx)

        # 만약에 다음에 꽂을 동일한 전기용품이 없다면 종료하기
        if not hasPlug:
            break

    # 플러그 뽑기
    # 가장 큰 값(가장 멀리 다시 꼽을 순서가 있는 플러그 or 다음에 꼽을 필요가 없는 플러그)을 먼저 뽑아내
    # 그 위치의 인덱스를 저장한다.
    outPlug = nextPlugs.index(max(nextPlugs))
    del nowPlug[outPlug] # 그 인덱스에 해당하는 플러그를 제거한다.
    nowPlug.append(name[i])
    count += 1

print(count)

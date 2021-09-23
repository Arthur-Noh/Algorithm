# 그리디 알고리즘
# 백준 2217번
# 등급 실버 4

# 문제 해결 아이디어
# 로프들을 이용하여 들어올릴수 있는 물체의 최대 중량을 구하여라
# 단 모든 로프를 사용해야 할 필요가 없다.

# 로프를 여러개(k)를 연결하면 각 로프에는 w/k 만큼 동일한 무게가 걸린다.
# 로프가 들 수 있는 무게 * 연결된 로프의 갯수(k) = 최대 중량(w)
# 따라서 가장 무거운 무게를 들 수 있는 로프부터 내림차순으로 정렬한 후
# 로프의 갯수를 추가하면서 가장 무거운 무게를 견딜수 있는 값을 출력하면 된다.

import sys

n = int(sys.stdin.readline())
rope = list(int(sys.stdin.readline()) for _ in range(n))

rope.sort(reverse=True)

for i in range(n):
    rope[i] *= (i+1)

print(max(rope))

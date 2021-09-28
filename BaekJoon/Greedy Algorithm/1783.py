# 그리디 알고리즘
# 백준 1783번
# 등급 실버 4

# 문제 해결 아이디어
# 병든 나이트는 오른쪽으로만 이동을 하고, 위 아래로는 자유롭게 움직일 수 있다.

# 1) 가로나 세로의 길이가 1인 경우
# 병든 나이트는 시작 칸 1개만 방문 할 수 있다.

# 2) 세로의 길이가 2인 경우
# 병든 나이트가 4번 이상로 움직인 경우 모든 방식을 다 사용해야 한다.
# 그러나 세로의 길이가 2인 경우 2, 3번의 방식 밖에 이용하지 못한다.(최대 3번)
# 나이트가 방문한 칸의 수 = 이동 가능 횟수 + 1
# 이동 가능 횟수는 (M-1)//2 가 된다.
# 4와 (M-1)//2 + 1중 작은 값을 구하면 된다.

# 3) 세로(N)의 길이가 3 이상, 가로(M)의 길이가 7 미만인 경우
# 세로의 길이가 3 이상인 경우, 가로로 1칸씩 이동하는 방식(1, 4번)이 가장 효율적이다.
# 그러나 나이트가 4번 이상 움직인 경우 모든 방식을 다 사용해야 한다.
# 따라서 세로의 길이가 3 이상이며, 가로의 길이가 7 미만인 경우
# 4와 가로의 길이(M) 중 작은 수를 출력하면 된다.

# 4) 세로(N)의 길이가 3 이상, 가로(M)의 길이가 7 이상인 경우
# N이 3보다 크다면 이동 경로에 영향을 주지 못한다.
# 그러나 나이트가 오른쪽으로만 이동을 할 수 있기 때문에 가장 많은 이동 횟수를 만들기 위해서는
# 1, 4번과 같이 오른쪽으로 1회만 이동하는 경우가 가장 효율적이다.
# 또한 2, 3번의 이동이 1회씩 실행되어야 하므로
# 최대 이동 횟수 = (2, 3번의 1회 이동) + (가로 길이 - 처음칸 - 2,3번 이동으로 인한 4칸)
# 최대 이동 횟수 = 2 + (M - 5) + 1

# 코드
# 체스판의 세로(N)과 가로(M) 입력
n, m = map(int, input().split())
move_count = 0

if n == 1:
    move_count = 1
elif n == 2:
    move_count = min(4, (m-1)//2 + 1)
elif n >= 3 and m < 7:
    move_count = min(4, m)
else:
    move_count = 2 + (m - 5) + 1

print(move_count)
# 코딩 테스트 준비 - 기초
# 백준 2309 일곱 난쟁이
# 등급 브론즈 2

# 문제 해결 아이디어
# 이중 포문을 사용한 부르트 포스를 이용해 해결한다.
# i 는 8번 까지만 돌리고, j 는 i 의 다음 값부터 9번 반복 연산을 수행하며
# 총 중량 w 에서 arr[i] 값과 arr[j] 값을 제외했을 때 100이 성립된다면
# 두 값을 리스트에서 제거하고, 오름차순 후 출력하면 된다.

import sys

# 난쟁이 키 입력
arr = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
w = sum(arr)

for i in range(8):
    for j in range(i + 1, 9):
        if w - arr[i] - arr[j] == 100:
            x1, x2 = arr[i], arr[j]

            arr.remove(x1)
            arr.remove(x2)

            arr.sort()

            for k in range(len(arr)):
                print(arr[k])

            break

    if len(arr) < 9:
        break

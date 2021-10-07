# 기초 수학 문제
# 백준 2309 일곱 난쟁이
# 등급 브론즈 2

# 문제 해결 아이디어
# 이중 포문을 사용하여 부르트 포스를 이용하여 해결한다.
# i는 8번까지만 돌리고, j는 i의 다음값 부터 9번 반복해보며
# 총 중량 w 에서 arr[i] 값과 arr[j] 값을 빼보았을 때 100이 성립되면
# 두 값을 리스트에서 제거하고, 오름차순 후 출력하면 된다.

import sys

# 난쟁이 키 리스트
arr = [int(sys.stdin.readline().rstrip()) for _ in range(9)]

w = sum(arr)

for i in range(8):
    for j in range(i + 1, 9):
        if w - arr[i] - arr[j] == 100:
            x1, x2 = arr[i], arr[j]

            arr.remove(x1)
            arr.remove(x2)

            arr.sort()  # 난쟁이의 키를 오름차순 정렬

            for k in range(len(arr)):
                sys.stdout.write("{0} ".format(arr[k]))
            break

    if len(arr) < 9:
        break

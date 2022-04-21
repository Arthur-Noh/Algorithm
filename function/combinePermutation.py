# 숫자 조합 함수

# 프로그래머스 - 코딩테스트연습/완전탐색/소수 찾기
# 문자열을 입력받으면 하나씩 분리하고, 가능한 모든 경우의 수를 조합하여 리턴한다.
# 여기서는 숫자 배열로 작성되었음


from itertools import permutations

def combinePermutation (lists):
  dataList = [data for data in lists]
  per = []
  
  for i in range(1, len(dataList) + 1)
    per += list(permutations(dataList, i))
   
  permutationNumbers = [int(("").join(p)) for p in per]
  
  return permutationNumbers

# 문제 해결 아이디어
# 1. 문자열로 구성된 숫자들을 모두 분리하고 모든 경우의 수에 해당하는 조합 리스트를 만든다.
# 2. 조합 리스트를 순회하면서 소수인지 판단하고 갯수를 센다.

import math
from itertools import permutations


# 1. 문자열로 구성된 숫자들을 모두 분리하고 모든 경우의 수에 해당하는 조합 리스트 만들기
# @see https://github.com/Arthur-Noh/Algorithm/blob/main/function/combinePermutation.py
def combinePermutation (numbers):
    numberList = [number for number in numbers]
    per = []  
    for i in range(1, len(numbers) + 1):
        per += list(permutations(numberList, i))
    
    permutationNumbers = [int(("").join(p)) for p in per]
    
    return permutationNumbers


# 2. 조합리스트의 숫자를 받아 소수인지 판단하고 반환하기
# @see https://github.com/Arthur-Noh/Algorithm/blob/main/function/checkPrime.py
def checkPrime (number):
    if number <= 1:
        return False
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    
    return True


def solution(numbers):
    numberList = set(combinePermutation(numbers))  # 조합된 리스트, 중복값이 있으므로 set로 제거한다.
    count = 0
    
    for number in numberList:
        if checkPrime(number):
            count += 1
    
    return count

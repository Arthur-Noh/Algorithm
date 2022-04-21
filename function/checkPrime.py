# 숫자 하나를 입력 받아 소수인지 판단하는 함수
# 그냥 2 ~ n 까지 비교해 볼 수도 있지만 시간복잡도는 O(N) 이다.
# 에라토스테네스의 체를 사용하면 시간복잡도는 O(N log log N)
# @see https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_complexity

import math

def checkPrime(number):
  for i in range(2 , int(math.sqrt(number)) + 1):
    if number % 2 == 0 :
      return False
    
  return True

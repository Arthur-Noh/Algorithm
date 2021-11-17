# 코딩 테스트 연습 - 프로그래머스
# 해시 - 전화번호 목록
# 성공

# 문제 해결 아이디어
# 어떤 문자열의 시작이 xxx로 시작한다는 것을 보고
# startswith 함수를 사용하면 더 쉽게 풀이할 수 있겠다 생각했다.
# 먼저 입력받은 전화번호부를 오름차순으로 정렬한다.
# 한 번호가 다른 번호의 접두로 시작한다면 이를 정렬했을 때 이 둘은 서로 붙게 된다.
# 따라서 오름차순 정렬을 먼저 수행한 뒤
# 앞번호와 뒷번호를 서로 짝지어 앞번호가 뒷 번호의 시작 번호인지 확인하는 함수를 작성하면 된다.

phone_book = ['12', '123', '1235', '567', '88']


def solution(phone_book):
    phone_book.sort()
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):  # 만약 p1이 p2의 접두로 시작한다면
            return False  # 바로 False return

    return True  # 아니라면 True


print(solution(phone_book))

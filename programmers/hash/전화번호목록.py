# 프로그래머스
# 코딩테스트 고득점 Kit
# 해시 : 전화번호 목록

# 문제 해결 아이디어
# 번호가 있는 배열이 있는데, 여기서 한 번호가 다른 번호의 접두사인 경우에는 false, 아닌경우 true를 반환하면 된다.
# 지난번에 완주자 명단과 같이 사용한 방식으로 해결하면 쉽다.

# 배열을 오름차순으로 정렬을 수행하고
# 첫번째 값은 배열 그대로, 두번째 값을 첫번째 값을 제외한 배열부터 시작해서
# 두번째 값의 시작이 첫번째 값으로 시작되면 false 를 반환하게 만들면 된다.

phoneBook = ["12", "123", "1235", "567", '88']


def solution(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return True


print(solution(phoneBook))

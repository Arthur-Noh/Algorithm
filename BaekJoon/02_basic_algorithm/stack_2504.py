# 기초 알고리즘 문제
# 백준 2504 괄호의 값
# 등급 실버 2

# 문제 해결 아이디어
# 기본 스택 문제

# ( 나 [ 가 나오면 스택에 입력을 받는다.

# ) 와 ] 가 나오면 두 경우로 나눠서 생각한다.
# ) 일 때
# stack[-1]이 ( 이면 () 되어 괄호의 값은 2가 된다.
# stack[-1]의 값을 2로 바꾼다.
# stack의 길이만큼 반복하면서 temp에 계속 더해주고 stack.pop을 수행한다.
# stack의 ( 를 만난 경우
# stack[-1] 에 그 동안 더해온 temp * 2를 넣어주고 반복문을 탈출한다.
# ] 일때도 동일하게 반복하면 된다.
import sys

s = sys.stdin.readline().rstrip()


# 올바른 괄호열인지 확인하는 함수
def is_check(s):
    stack = []
    check = True

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])

        else: # ) ]
            if s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    check = False

            else: # ]
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    check = False

    if not stack and check: # 스텍이 비어있거나 체크가 True 면
        return True
    else:
        return False


# 괄호의 값을 계산하는 함수
def cal_value(s):
    stack = []

    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[':
            stack.append(s[i])

        else: # ) ]
            if s[i] == ')':
                if stack[-1] == '(':
                    stack[-1] = 2

                else:  # 올바른 괄호열 이기 때문에 숫자만 있다.
                    temp = 0
                    for idx in range(len(stack)-1, -1, -1):  # 괄호를 만날 때까지 더해주기
                        if stack[idx] == '(':
                            stack[-1] = temp * 2
                            break
                        else:
                            temp += stack[-1]
                            stack.pop()
            else : # ]
                if stack[-1] == '[':
                    stack[-1] = 3

                else:  # 올바른 괄호열 이기 때문에 숫자만 있다.
                    temp = 0
                    for idx in range(len(stack)-1, -1, -1): # 괄호를 만날 때까지 계속 더해주기
                        if stack[idx] == '[':
                            stack[-1] = temp * 3
                            break
                        else:  # type(stack[idx]) == int
                            temp += stack[-1]
                            stack.pop()

    return sum(stack)


if is_check(s):
    print(cal_value(s))
else:
    sys.stdout.write("0\n")

"""
    문제
        계산기 프로그램을 작성하시오.

    요구사항
        1. 계산식을 정규식을 사용해서 정수와 사칙 연산을 분리 합니다.

    출력 예시:
        Case 1)
            계산식을 입력하세요
            1 + 1 (Enter)
            2

        Case 2)
            계산식을 입력하세요
            2 * 3 (Enter)
            6
"""
import re

# 정규식을 시험할 계산식입니다.
expression = input("계산식을 입력하세요: ")

# fullmatch는 expression의 처음부터 끝까지가 정규식 모양과 맞는지 검사합니다.
# 맞으면 Match 객체를 돌려주고, 맞지 않으면 None을 돌려줍니다.
# 앞의 r은 역슬래시(\)를 파이썬 문자열에서 특별 처리하지 말고
# 정규식에 그대로 전달하라는 뜻입니다.
#
# 정규식 r"\s*(-?\d+)\s*([+*/-])\s*(-?\d+)\s*"를 왼쪽부터 읽으면:
#   \s*       공백 문자가 0개 이상 있어도 됩니다.
#   (-?\d+)   괄호로 묶인 첫 번째 숫자입니다.
#             -?는 마이너스 기호가 있어도 되고 없어도 된다는 뜻이고,
#             \d+는 숫자가 한 자리 이상 있다는 뜻입니다.
#   \s*       숫자와 연산자 사이의 공백입니다(없어도 됩니다).
#   ([+*/-])  괄호로 묶인 연산자 한 개입니다: +, -, *, /
#   \s*       연산자와 두 번째 숫자 사이의 공백입니다(없어도 됩니다).
#   (-?\d+)   괄호로 묶인 두 번째 숫자입니다.
#   \s*       식 앞뒤에 공백이 있어도 됩니다.
# 괄호로 묶은 부분은 나중에 group(1), group(2), group(3)으로 꺼냅니다.
match = re.fullmatch(r"\s*(-?\d+)\s*([+*/-])\s*(-?\d+)\s*", expression)

# match가 None이 아니라면 계산식 전체가 위 정규식에 맞았다는 뜻입니다.
if match:
    # group(1)은 첫 번째 괄호에 잡힌 값("2")입니다.
    # 정규식에서 꺼낸 값은 문자열이므로 int()로 정수로 바꿉니다.
    first = int(match.group(1))

    # group(2)는 두 번째 괄호에 잡힌 연산자("*")입니다.
    operator = match.group(2)

    # group(3)은 세 번째 괄호에 잡힌 값("3")입니다.
    second = int(match.group(3))

    # 연산자에 따라 first와 second를 계산합니다.
    try:
        if operator == "+":
            result = first + second
        elif operator == "-":
            result = first - second
        elif operator == "*":
            result = first * second
        else:
            result = first / second

        # :g는 결과가 2.0일 때 2로 간단히 표시합니다.
        print(f"{result:g}")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
else:
    # 계산식이 정규식 모양과 맞지 않으면 이쪽을 실행합니다.
    print("잘못된 계산식입니다.")
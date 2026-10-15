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


def print_calculator(math_value):
    match math_value[1]:
        case "+":
            print(int(math_value[0]) + int(math_value[2]))
        case "-":
            print(int(math_value[0]) - int(math_value[2]))
        case "*":
            print(int(math_value[0]) * int(math_value[2]))
        case "/":
            print(int(math_value[0]) / int(math_value[2]))


def main():
    CALC_MESSAGE = "계산식을 입력하세요:\n"
    REGULAR_EXPRESSION = r"([-+*/])"

    math_prompt = input(CALC_MESSAGE)

    math_value = re.split(REGULAR_EXPRESSION, math_prompt)
    if len(math_value) != 3:
        print("계산식을 올바르게 입력하세요.\n\n")
        return

    print_calculator(math_value)


if __name__ == "__main__":
    main()
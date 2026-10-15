"""
    문제
        계산기 프로그램을 작성하시오.

    요구사항
        1. 숫자와 사칙 연산 사이에 " " 공백이 들어가야 합니다.
        2. 계산식을 split 함수 사용해서 숫자와 문자를 분리 합니다.
        3. 사칙 연산에 조건문이 사용되는 경우 if 문을 사용 합니다.

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


def print_calculator(math_value):
    if math_value[1] == "+":
        print(int(math_value[0]) + int(math_value[2]))
    elif math_value[1] == "-":
        print(int(math_value[0]) - int(math_value[2]))
    elif math_value[1] == "*":
        print(int(math_value[0]) * int(math_value[2]))
    elif math_value[1] == "/":
        print(int(math_value[0]) / int(math_value[2]))


def main():
    CALC_MESSAGE = "계산식을 입력하세요:\n"
    math_prompt = input(CALC_MESSAGE)

    math_value = math_prompt.split(" ")
    if len(math_value) != 3:
        print("계산식을 올바르게 입력하세요.\n\n")
        return

    print_calculator(math_value)

if __name__ == "__main__":
    main()
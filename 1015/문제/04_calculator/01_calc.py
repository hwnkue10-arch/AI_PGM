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


def calculate(expression):
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError

    first = float(parts[0])
    operator = parts[1]
    second = float(parts[2])

    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        result = first / second
    else:
        raise ValueError

    return result


def main():
    print("계산식을 입력하세요")
    expression = input()

    try:
        result = calculate(expression)
        print(f"{result:g}")
    except ValueError:
        print("잘못된 계산식입니다.")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")


if __name__ == "__main__":
    main()
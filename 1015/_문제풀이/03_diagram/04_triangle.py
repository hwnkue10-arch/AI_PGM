"""
    요구사항
        for문을 이용하여 정삼각형을 출력하는 프로그램을 작성하시오

    요구사항
        1. 반복문(for과 while)을 사용하여 작성하시오.
        2. 삼각형을 출력하는 핵심 로직은 별도의 함수로 구현하시오.
        3. 함수의 매개변수(parameter)로 삼각형의 크기를 전달받도록 하시오.
        4. 함수 내부에서 '#' 문자를 사용하여 삼각형을 출력하시오.

    출력 예시:
        정삼각형의 크기를 입력하세요: 7

                      # 
                    # # # 
                  # # # # # 
                # # # # # # # 
              # # # # # # # # # 
            # # # # # # # # # # # 
          # # # # # # # # # # # # # 
        # # # # # # # # # # # # # # # 
"""


def print_trangle(triangle_size):
    cnt = 1

    for line in range(triangle_size, -1, -1):
        print("  " * line, end="")
        print("# " * cnt)
        cnt += 2


if __name__ == "__main__":
    USER_QUESTION = "(좌측 정렬) 직각삼각형의 크기를 입력하세요: "
    triangle_size = int(input(USER_QUESTION))

    print_trangle(triangle_size)
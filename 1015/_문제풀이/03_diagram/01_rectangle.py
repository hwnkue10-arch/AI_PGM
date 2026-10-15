"""
    문제
        사용자로부터 정수를 입력받아, 그 크기만큼 '#' 문자로 정사각형을 출력하는 코드를 작성하시오.

    출력 예시:
        정사각형의 크기를 입력하세요: 10

        # # # # # # # # # # 
        # # # # # # # # # # 
        # # # # # # # # # # 
        # # # # # # # # # # 
        # # # # # # # # # # 
        # # # # # # # # # # 
        # # # # # # # # # # 
        # # # # # # # # # # 
        # # # # # # # # # # 
        # # # # # # # # # # 
"""

def print_rectangle(rectangle_size):
    for _ in range(1, rectangle_size + 1):
        print("# " * rectangle_size)


if __name__ == "__main__":
    USER_QUESTION = "정사각형의 크기를 입력하세요: "
    rectangle_size = int(input(USER_QUESTION))

    print_rectangle(rectangle_size)
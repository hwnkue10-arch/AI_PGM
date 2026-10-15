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
def make_triangle(parameter):
    for j in range(1, parameter+1):
        print()
        print("  " * (parameter - j),"# " * (2*j-1), end="")

def main():
    try:
        num = int(input("이등변 삼각형의 크기를 입력하세요: "))
        if num > 0:
          make_triangle(num)
        else:
          print("양수를 입력하세요.")
        
    except ValueError:
        print("정수를 입력하세요.")
        
if __name__ == "__main__":
    main()
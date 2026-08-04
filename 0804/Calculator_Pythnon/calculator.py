class Calculator:


    def __init__(self):

        self.expression = ""



    # 입력 추가

    def add_input(self, value):


        normal_operators = "+*/"



        # -----------------------------
        # + * / 처리
        # -----------------------------

        if value in normal_operators:


            if self.expression == "":

                return



            # 이전이 연산자면 교체

            if self.expression[-1] in "+*/":


                self.expression = (

                    self.expression[:-1]

                    + value

                )

                return



            # 이전이 음수 표시라면 처리

            if self.expression.endswith("-"):


                if len(self.expression) >= 2:


                    if self.expression[-2] in "+*/":


                        self.expression = (

                            self.expression[:-2]

                            + value

                        )

                        return



            self.expression += value

            return





        # -----------------------------
        # - 처리
        # -----------------------------

        if value == "-":


            if self.expression == "":

                self.expression = "-"

                return



            if self.expression.endswith("-"):

                return



            if self.expression[-1] in "+*/":

                self.expression += "-"

                return



            self.expression += "-"

            return





        # -----------------------------
        # 소수점 처리
        # -----------------------------

        if value == ".":


            # 마지막 숫자 구간 확인

            number = ""


            for char in reversed(self.expression):


                if char.isdigit() or char == ".":

                    number = char + number


                else:

                    break



            # 이미 소수점 존재

            if "." in number:

                return



            # 처음 . 입력

            if self.expression == "" or self.expression[-1] in "+-*/":

                self.expression += "0"



            self.expression += "."

            return





        # -----------------------------
        # 숫자 처리
        # -----------------------------

        if value.isdigit():


            # 0 뒤 숫자 처리

            if self.expression == "0":

                self.expression = value

                return



        self.expression += value





    # 현재 식 반환

    def get_expression(self):

        return self.expression





    # 계산

    def calculate(self):

        try:


            if self.expression == "":

                return "Error"



            result = eval(

                self.expression,

                {

                    "__builtins__": None

                },

                {}

            )



            if isinstance(result,float):


                result = round(result,10)



                # 5.0 -> 5

                if result.is_integer():

                    result = int(result)



            self.expression = str(result)


            return self.expression




        except ZeroDivisionError:


            return "Error"




        except Exception:


            return "Error"






    # 초기화

    def clear(self):

        self.expression = ""






    # 삭제

    def backspace(self):


        if self.expression:


            self.expression = self.expression[:-1]







    # 부호 변경

    def change_sign(self):


        if self.expression == "":

            return



        operators = "+-*/"



        # 마지막 숫자 위치 찾기

        index = len(self.expression)-1



        while index >= 0:


            if self.expression[index] in operators:

                break


            index -= 1



        # 마지막 숫자

        number = self.expression[index+1:]



        if number == "":

            return



        # 이미 음수면 제거

        if number.startswith("-"):


            number = number[1:]

            self.expression = (

                self.expression[:index+1]

                + number

            )


        else:


            self.expression = (

                self.expression[:index+1]

                + "-"

                + number

            )
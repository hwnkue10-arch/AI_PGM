import tkinter as tk

from calculator import Calculator
from button import CalculatorButton


class CalculatorUI:


    def __init__(self, root):

        self.root = root

        self.calculator = Calculator()


        # 창 설정

        self.root.title("Python Calculator")

        self.root.geometry("430x700")

        self.root.resizable(False, False)

        self.root.configure(
            bg="#202020"
        )



        self.create_widgets()



    # 화면 구성
    def create_widgets(self):


        # 수식 표시창

        self.expression_label = tk.Label(

            self.root,

            text="",

            anchor="e",

            font=("Segoe UI", 18),

            bg="#202020",

            fg="gray"

        )


        self.expression_label.pack(

            fill="x",

            padx=15,

            pady=(10,0)

        )



        # 결과 입력창

        self.display = tk.Entry(

            self.root,

            font=("Segoe UI", 32),

            justify="right",

            bg="#303030",

            fg="white",

            insertbackground="white"

        )


        self.display.pack(

            fill="x",

            padx=20,

            pady=5,

            ipady=10

        )



        self.display.insert(

            0,

            "0"

        )



        # 버튼 영역

        frame = tk.Frame(

            self.root,

            bg="#202020"

        )


        frame.pack(

            pady=10

        )



        buttons = [

            ("7",1,0),
            ("8",1,1),
            ("9",1,2),
            ("/",1,3),

            ("4",2,0),
            ("5",2,1),
            ("6",2,2),
            ("*",2,3),

            ("1",3,0),
            ("2",3,1),
            ("3",3,2),
            ("-",3,3),

            ("C",4,0),
            ("0",4,1),
            (".",4,2),
            ("+",4,3),

            ("←",5,0),
            ("±",5,1),
            ("(",5,2),
            (")",5,3),

            ("=",6,0)

        ]



        for text,row,col in buttons:


            # 버튼 종류 결정

            if text == "C":

                button_type = "clear"


            elif text == "=":

                button_type = "equal"


            elif text in ["+","-","*","/"]:

                button_type = "operator"


            else:

                button_type = "number"



            button = CalculatorButton(

                frame,

                text,

                lambda value=text:
                    self.button_click(value),

                button_type

            )   


            button.grid(

                row=row,

                column=col,

                padx=3,

                pady=3

            )



    # 버튼 이벤트
    def button_click(self, value):

        print("클릭:", value)


        if value == "C":

            self.calculator.clear()


        elif value == "←":

            self.calculator.backspace()


        elif value == "±":

            self.calculator.change_sign()


        elif value == "=":

            self.calculator.calculate()


        else:

            self.calculator.add_input(value)


        self.update_display()



    # 화면 갱신
    def update_display(self):


        expression = self.calculator.get_expression()


        self.expression_label.config(

            text=expression

        )


        self.display.delete(

            0,

            tk.END

        )


        if expression == "":

            self.display.insert(

                0,

                "0"

            )

        else:

            self.display.insert(

                0,

                expression

            )
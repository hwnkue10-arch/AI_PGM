import tkinter as tk


class CalculatorButton(tk.Button):

    def __init__(
        self,
        parent,
        text,
        command,
        button_type="number"
    ):

        colors = {

            "number": "#505050",
            "operator": "#ff9500",
            "equal": "#0078d7",
            "clear": "#d63031"

        }


        self.normal_color = colors.get(
            button_type,
            "#505050"
        )


        self.hover_color = "#707070"


        super().__init__(

            parent,

            text=text,

            command=command,

            width=6,

            height=2,

            font=("Segoe UI",14),

            fg="white",

            bg=self.normal_color,

            activeforeground="white",

            activebackground=self.hover_color,

            relief="flat",

            cursor="hand2"

        )


        # Hover 이벤트

        self.bind(
            "<Enter>",
            self.on_hover
        )

        self.bind(
            "<Leave>",
            self.on_leave
        )



    # 마우스 올라감

    def on_hover(self,event):

        self.config(
            bg=self.hover_color
        )



    # 마우스 나감

    def on_leave(self,event):

        self.config(
            bg=self.normal_color
        )
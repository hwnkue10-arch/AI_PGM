import tkinter as tk
from tkinter.colorchooser import askcolor

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("그림판")

        self.color = "black"
        self.eraser = False
        self.size = 5

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack()

        frame = tk.Frame(root)
        frame.pack()

        tk.Button(frame, text="색 선택", command=self.pick_color).pack(side="left")
        tk.Button(frame, text="펜", command=self.pen).pack(side="left")
        tk.Button(frame, text="지우개", command=self.erase).pack(side="left")
        tk.Button(frame, text="전체 지우기", command=self.clear).pack(side="left")

        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.x = None
        self.y = None

    def pick_color(self):
        c = askcolor()[1]
        if c:
            self.color = c
            self.eraser = False

    def pen(self):
        self.eraser = False

    def erase(self):
        self.eraser = True

    def clear(self):
        self.canvas.delete("all")

    def draw(self, event):
        if self.x and self.y:
            color = "white" if self.eraser else self.color
            self.canvas.create_line(
                self.x, self.y, event.x, event.y,
                fill=color, width=self.size, capstyle=tk.ROUND
            )
        self.x, self.y = event.x, event.y

    def reset(self, event):
        self.x = None
        self.y = None


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
    
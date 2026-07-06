import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("간단 메모장")
        self.file_path = None

        self.text = tk.Text(root, wrap="word")
        self.text.pack(expand=True, fill="both")

        menubar = tk.Menu(root)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="새 파일", command=self.new_file)
        filemenu.add_command(label="열기", command=self.open_file)
        filemenu.add_command(label="저장", command=self.save_file)
        filemenu.add_command(label="다른 이름으로 저장", command=self.save_as)
        filemenu.add_separator()
        filemenu.add_command(label="종료", command=root.quit)

        menubar.add_cascade(label="파일", menu=filemenu)
        root.config(menu=menubar)

    def new_file(self):
        self.text.delete("1.0", tk.END)
        self.file_path = None

    def open_file(self):
        path = filedialog.askopenfilename()
        if path:
            with open(path, "r", encoding="utf-8") as f:
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, f.read())
            self.file_path = path

    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", tk.END))
        else:
            self.save_as()

    def save_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.text.get("1.0", tk.END))
            self.file_path = path


if __name__ == "__main__":
    root = tk.Tk()
    app = Notepad(root)
    root.mainloop()
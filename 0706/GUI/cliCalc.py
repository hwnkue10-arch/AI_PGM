import tkinter as tk

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(entry_var.get()))
            entry_var.set(result)
        except:
            entry_var.set("Error")

    elif text == "C":
        entry_var.set("")

    else:
        entry_var.set(entry_var.get() + text)


root = tk.Tk()
root.title("GUI Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()

entry = tk.Entry(root, textvar=entry_var, font="Arial 20")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

frame = tk.Frame(root)
frame.pack()

for i, b in enumerate(buttons):
    btn = tk.Button(frame, text=b, font="Arial 18", width=5, height=2)
    btn.grid(row=i//4, column=i%4)
    btn.bind("<Button-1>", click)

root.mainloop()
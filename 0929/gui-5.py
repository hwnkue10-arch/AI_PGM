from tkinter import *
win=Tk()
win.geometry("400x400")
win.title("test")
chkvar=BooleanVar()
chkbox=Checkbutton(win, text="don't show for today", variable=chkvar)
chkbox.pack()
def btncmd():
    print(chkvar.get())
btn=Button(win, text="click", command=btncmd)
btn.pack()
win.mainloop()
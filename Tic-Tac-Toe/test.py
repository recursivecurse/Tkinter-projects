import tkinter as tk
root = tk.Tk()

def update_btn_text():
    if(btn["text"]=="a"):
        btn.configure(text="b")
    else:
        btn.configure(text="a")


btn = tk.Button(root, text="a", command=update_btn_text)
btn.pack()

root.mainloop()

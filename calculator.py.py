import tkinter as tk

memory = 0  # Global memory variable

def click(event):
    global memory
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "M+":
        try:
            memory = float(entry.get())
        except:
            memory = 0
    elif text == "MR":
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(memory))
    elif text == "MC":
        memory = 0
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Enhanced Calculator")
root.geometry("300x500")

entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["M+", "MR", "MC"]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack()
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font="Arial 18", width=5, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()

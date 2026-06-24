
frame = tk.Frame(root)
frame.pack()

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

r, c = 0, 0
for b in buttons:
    cmd = calculate if b == "=" else lambda x=b: entry.insert(tk.END, x)
    tk.Button(frame, text=b, width=5, height=2, command=cmd).grid(row=r, column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1

tk.Button(root, text="Clear", command=clear).pack(fill="both", padx=10, pady=10)

root.mainloop()import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20))
entry.pack(fill="both", padx=10, pady=10)

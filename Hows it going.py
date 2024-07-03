import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("My First GUI")

Label = tk.Label(root, text="Hows it going", font=('Arial', 18))
Label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3,  font=('Arial', 16))
textbox.pack(padx=10, pady=10)

button = tk.Button(root, text="Good!", font=('Arial', 16))
button.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)


root.mainloop()

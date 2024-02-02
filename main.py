import tkinter


window tkinter.Tk()
s tkinter.StringVar()
x = []

def button click():
    n=int(s.get())
    for i in range(n):
    x.append(int(input()))

label-tkinter.Label(window, text='Введіть кількість елементів:')

label.pack()
edit-tkinter. Entry (window, textvariable=s)

edit.pack()

button-tkinter.Button (window, text="Розпочати введення", command button click)

button.pack()
window.mainloop()

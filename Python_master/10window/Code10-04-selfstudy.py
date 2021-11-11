from tkinter import *
from tkinter import font
window = Tk()
window.title("윈도우 연습")
# window.geometry("400x200")
# window.resizable(width= FALSE, height= True)

label1 = Label(window, text = "COOKBOOK!")
label2 = Label(window, text = "열심히", font = ("궁서체",30), fg = "blue")
label3 = Label(window, text = "공부중 입니다.", bg="magenta", width=20, height=5, anchor= SE)

label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack()


# photo = PhotoImage(file= "../10window/smiling-cat-creepy-cat.gif")
# label1 = Label(window, image= photo)

label1.pack()
window.mainloop()
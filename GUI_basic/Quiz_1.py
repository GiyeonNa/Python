import os
from tkinter import *

root = Tk()
root.title("제목없음 - windosw 메모장") #이름
root.geometry("640x480")

filename = "mynote.txt"

#저장
def save_file():
    with open(filename,"w",encoding="utf8") as note:
       note.write(txt.get("1.0", END))

#열기
def load_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as note:
            txt.delete("1.0",END)
            txt.insert(END, note.read())

#메뉴 생성
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=load_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)

menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")


# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

#텍스트
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both", expand=True, side="left")

scrollbar.config(command=txt.yview)


root.config(menu=menu)
root.mainloop()
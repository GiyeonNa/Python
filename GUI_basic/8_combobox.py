import tkinter.ttk as ttk #combobox는 필요함
from tkinter import *

root = Tk()
root.title("Nado GUI") #이름
root.geometry("640x480")

values = [str(i) + "일" for i in range(1,32)] #1~31 
combobox = ttk.Combobox(root, height=5 ,values=values ,state="readonly") #state="readonly" 하면 사용자가 입력하지 못한다
combobox.pack()
combobox.set("카드 결제일") #최초 목록 제목 설정

def btncmd():
    print(combobox.get()) #선택된 값 표시

btn = Button(root, text="Button", command=btncmd)
btn.pack()

root.mainloop() #mainloop를 통해 창 닫히는걸 방지

from tkinter import *

root = Tk()
root.title("Nado GUI") #이름
root.geometry("640x480")

label1 = Label(root, text="안녕하세요") #안녕하세요 글자 출력
label1.pack()

photo = PhotoImage(file="GUI_basic/image.png") #그림주소를 받아서 그림도 출려가능
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2 #전역변수로 설정
    photo2 = PhotoImage(file="GUI_basic/cross.png")
    label2.config(image=photo2) #전역변수로 만들지 않으면 변하지않음

btn = Button(root, text="클릭", command=change) #버튼을 누르면 chage이벤트 발생
btn.pack()

root.mainloop() #mainloop를 통해 창 닫히는걸 방지

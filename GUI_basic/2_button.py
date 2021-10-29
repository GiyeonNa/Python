from tkinter import *

root = Tk()
root.title("Nado GUI") #이름
# root.geometry("640x480") #가로 * 세로
# root.geometry("640x480+300+300") #가로 * 세로 + x좌표 + y좌표
# root.resizable(True,True) # X(너비) Y(높이) 크기변경 금지

btn1 = Button(root, text="버튼1")  #넣을위치 , 버튼에 들어갈 명칭
btn1.pack() 

btn2 = Button(root, padx=5, pady=10, text="버튼2")  
btn2.pack() 
#padx, pady 버튼에 공간을 확보하여 설정

btn3 = Button(root, padx=10, pady=20, text="버튼3")  
btn3.pack() 

btn4= Button(root, width=10, height=3, text="버튼4")
btn4.pack()
#width, height 버튼 크기자체를 설정 

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()
#fg 글자색 bg 배경색


photo = PhotoImage(file="GUI_basic/image.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 눌려짐")

btn7 = Button(root, text="동작", command=btncmd)
btn7.pack()

root.mainloop() #mainloop를 통해 창 닫히는걸 방지

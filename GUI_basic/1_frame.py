from tkinter import *

root = Tk()
root.title("Nado GUI") #이름
# root.geometry("640x480") #가로 * 세로
root.geometry("640x480+300+300") #가로 * 세로 + x좌표 + y좌표

root.resizable(True,True) # X(너비) Y(높이) 크기변경 금지

root.mainloop() #mainloop를 통해 창 닫히는걸 방지

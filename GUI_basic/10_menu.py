from tkinter import *

root = Tk()
root.title("Nado GUI") #이름
root.geometry("640x480")

def create_new_file():
    print("새 파일을 만듭니다")

menu = Menu(root)

#File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New file", command=create_new_file)
menu_file.add_command(label="New window")
menu_file.add_separator() # 구분자 ---------------
menu_file.add_command(label="Open file...")
menu_file.add_separator()
menu_file.add_command(label="Save all", state="disable") #비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) #root.quit 프로그램 종료
menu_file.add_separator()

menu.add_cascade(label="File", menu=menu_file) 
#menu 에 File이라는 이름에 큰그룹에는 만들었던 menu_file이 들어있다


#Edit 메뉴
menu.add_cascade(label="Edit")

#language 메뉴 radio 버튼 응용
laguage_file = Menu(menu, tearoff=0)
laguage_file.add_radiobutton(label="Python")
laguage_file.add_radiobutton(label="qwer", state="disable")
laguage_file.add_separator()
laguage_file.add_radiobutton(label="zxcv")

menu.add_cascade(label="Laguage", menu=laguage_file)

#view 메뉴 checkbox 응용
check_file = Menu(menu, tearoff=0)
check_file.add_checkbutton(label="1")
check_file.add_checkbutton(label="2")
check_file.add_checkbutton(label="3")
check_file.add_checkbutton(label="4")

menu.add_cascade(label="Check", menu=check_file)


root.config(menu=menu)
root.mainloop() #mainloop를 통해 창 닫히는걸 방지

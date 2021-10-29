from tkinter import *

root = Tk()
root.title("Nado GUI") #이름
root.geometry("640x480")

label1 = Label(root, text="메뉴를 선택하세요")
label1.pack()
# Label(root, text="메뉴를 선택").pack() 위와 같은 역활

burger_var = IntVar() # int 형으로 값을 저장
btn1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn1.select() #기본으로 설정되어있게 하기
btn2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var) 
#value 에 따라 선택이 달라짐

btn1.pack()
btn2.pack()
btn3.pack()

label2 = Label(root, text="음료 선택")
label2.pack()

drink_var = StringVar() #문자일경우 StringVar()
drink1 = Radiobutton(root, text="콜라", value="콜라" , variable=drink_var)
drink1.select() #기본값
drink2 = Radiobutton(root, text="사이다", value="사이다" , variable=drink_var)

drink1.pack()
drink2.pack()


def btncmd():
    print(burger_var.get()) #햄버거 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get()) #음료 중 선택된 라디오 항목의 값(value) 출력

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop() #mainloop를 통해 창 닫히는걸 방지

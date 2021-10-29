import tkinter.messagebox as msbox #메시지 박스 필요
from tkinter import *

root = Tk()
root.title("Nado GUI") #이름
root.geometry("640x480")

#예매 시스템
def info():
    msbox.showinfo("알림","예매 완료") #"타이틀" ,"출력문"

def warn():
    msbox.showwarning("경고", "예매 실패")

def err():
    msbox.showerror("에러","에러 발생") 

def okcancel():
    msbox.askokcancel("확인 / 취소","해당 좌석은 가능한가요?")

def retry():
    msbox.askretrycancel("재시도 / 취소", "일시적 오류!")

def yesno():
    msbox.askyesno("예 / 아니오", "에 아니오 확인중")

def yesnocancel():
    response = msbox.askyesnocancel(title=None, message="예 아니오 취소 \n박스생성")
    # 예 : 저장 후 종료 , True
    # 아니오 : 저장 하지 않고 종료 , False
    # 취소 : 프로그램 종료 취소 , None
    print("응답", response)
    if response == 1: #예
        print("예")
    elif response == 0: #아니오
        print("아니오")
    else: #취소
        print("취소")

btn1 = Button(root, text="버튼", command=info)
btn1.pack()

btn2 = Button(root, text="버튼2", command=warn)
btn2.pack()

btn3 = Button(root, text="버튼3", command=err)
btn3.pack()

btn4 = Button(root, text="버튼4", command=okcancel)
btn4.pack()

Button(root, text="버튼5", command=retry).pack()
Button(root, text="버튼6", command=yesno).pack()
Button(root, text="버튼7", command=yesnocancel).pack()

root.mainloop() #mainloop를 통해 창 닫히는걸 방지

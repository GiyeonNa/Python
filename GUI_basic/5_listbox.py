from tkinter import *

root = Tk()
root.title("Nado GUI") #이름
root.geometry("640x480")

#리스트 박스 여러줄의 걸쳐 목록을 관리하는 위젯
listbox = Listbox(root, selectmode="extended", height=0) 
#extended 여러개 선택, single 하나만 선택
#height=0 이면 추가한 모든 요소를 보여줌 , height=n 이면 n개만 보여줌
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박") #END 는 마지막에 추가함
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    #삭제
    # listbox.delete(END) #END : 맨 뒤에 요소를 삭제 , 0 : 맨 앞에서 부터 삭제

    #갯수 확인
    # print("리스트에는", listbox.size(), "개가 있다")

    #항목 확인
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2)) #0부터 2까지

    #선택된 항목 확인 (인덱스 위치로 출력)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() #mainloop를 통해 창 닫히는걸 방지

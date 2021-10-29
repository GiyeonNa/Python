from tkinter import *

root = Tk()
root.title("Nado GUI") #이름
root.geometry("640x480")

txt = Text(root, width=30, height=5) #텍스트 위젯 생성
txt.pack()

txt.insert(END, "글자를 입력하세요") #사전에 미리 글자를 넣어둠

e = Entry(root, width=30) #Entry 는 한줄로 입력받음 -> enter 안 먹음
e.pack()
e.insert(0, "한 줄만 입력") #값이 비어있으므로 END를 써도 무방

def btncmd():
    #내용출력
    print(txt.get("1.0",END)) #처음부터 끝까지 모든 텍스트 가져오기, 1:첫번째 라인 0 : 0번째 colum위치
    print(e.get())

    #내용삭제
    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() #mainloop를 통해 창 닫히는걸 방지

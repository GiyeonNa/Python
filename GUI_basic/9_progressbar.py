import time
import tkinter.ttk as ttk #progresssbar 필요함
from tkinter import *

root = Tk()
root.title("Nado GUI") #이름
root.geometry("640x480")

progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") 
#언제끝날지 모르는작업에는  mode="indeterminate" 사용
#게이지 바 가 움직임
progressbar.start(10) #10ms 마다 움직임
progressbar.pack()

progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
#게이지가 차오르는 형식으로 진행도를 보여줌
# mode를 안적을경우 determinate가 기본값임
progressbar2.start(10) #10ms 마다 움직임
progressbar2.pack()

def btncmd():
    progressbar.stop()
    progressbar2.stop() 
    #작동 중지

btn = Button(root, text="Button", command=btncmd)
btn.pack()

progress_var = DoubleVar() #퍼센트가 항상 정수로 오르는것이 아닌 1.5 , 33.4 등 소수로도 오를수있기에 Double
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=progress_var)
progressbar3.pack()

def btncmd():
    for i in range(1,101):
        time.sleep(0.01) # 0.01초 대기
        progress_var.set(i) #progress bar 의 값 설정
        progressbar3.update() #for 문 동작할때 마다 GUI 업데이트
        print(progress_var.get())


btn = Button(root, text="Button", command=btncmd)
btn.pack()

root.mainloop() #mainloop를 통해 창 닫히는걸 방지

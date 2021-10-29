import os
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk 
from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("Project")

#파일추가
#사용자에게 오픈할 파일을 선택하세함
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",\
        filetypes=(("PNG 파일","*png"),("모든 파일","*.*")),\
            initialdir=r"C:\Users\nagiy\OneDrive\Desktop\Python_workspace")    
            #최초에 사용자가 지정한 경로를 보여줌 , r을 사용하면 탈출문자 //두번안써도 이해함

    #사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END,file)

#파일 삭제
def del_file():
    print(list_file.curselection())

    for index in reversed(list_file.curselection()): #reversed는 실제값에는 영향을 미치지않는다
        list_file.delete(index)

#저장경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "": #사용자가 취소를 누를떄
        return
    
    txt_dest_paht.delete(0,END)
    txt_dest_paht.insert(0,folder_selected)

#이미지 통합
def merge_image():
    # print("가로넓이 : ",cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("포맷 : ", cmb_format.get())

    #가로넓이
    img_width = cmb_width.get()
    if img_width == "원본 유지":
        img_width = -1 #-1 일때는 원본 기준으로
    else:
        img_width = int(img_width)

    #간격
    img_space = cmb_space.get()
    if img_space == "좁게":
        img_space = 30
    elif img_space == "보통":
        img_space = 50
    elif img_space == "넓게":
        img_space = 100
    else:
        img_space = 0

    #포맷
    img_fomat = cmb_format.get().lower() #소문자로 변경
    

    #모든 파일목록
    images = [Image.open(x) for x in list_file.get(0, END)]
    # size -> size[0] width , size[1] height

    image_size = [] #(width1, height1), (widht2, height2),(...)
    if img_width > -1:
        image_size = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images] #width 변경
    else:
        #원본크기 사용
        image_size = [(x.size[0], x.size[1]) for x in images] 

    #비율 계산식
    #원본 x : 원본 y = 바뀐 x : 바뀐 y
    # 100   :  60   =   80   :   ?
    #  x    :   y   =    x'  :   y'
    #  xy'  =  x'y 
    #   y'  =  x'y  /  x  -> 이걸 비율식의 적용 
    # x = width = size[0]
    # y = height = siz[1]
    # x' = img_width 
    # y' = img_widht * size[1] / size[0]

    # width = [x.size[0] for x in images]
    # height = [x.size[1] for x in images]
    # width , height = zip(*(x.size for x in images))
    width , height = zip(*image_size)

    #최대 넓이 , 전체 높이 
    max_width, total_height = max(width), sum(height)
    
    #여백
    if img_space > 0: #이미지 간격 조정
        total_height += (img_space * (len(images)-1))
    result_img = Image.new("RGB",(max_width, total_height), (255,255,255)) #배경 흰색
    y_offset = 0 #y 위치
    # for img in images:
    #     result_img.paste(img,(0,y_offset))
    #     y_offset += img.size[1]  # height 값만큼 추가

    for index, img in enumerate(images):
        #width가 원본유자가 아닐땐 크기조정
        if img_width > 0:
            img = img.resize(image_size[index])

        result_img.paste(img,(0,y_offset))
        y_offset += (img.size[1] + img_space) # 높이 + 간격

        progress = (index+1) / len(images) * 100 #실제 %정보 반영
        p_var.set(progress)
        progress_bar.update()

    #포맷 옵션
    file_name = "nado_photo." + img_fomat
    dest_path = os.path.join(txt_dest_paht.get(),file_name)
    result_img.save(dest_path)
    msgbox.showinfo("알림","저장완료")


def start():
    #각 옵션들 확인
    # print("가로넓이 : ",cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("포맷 : ", cmb_format.get())

    #파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고","이미지 파일을 추가하세요")
        return

    #저장경로 확인
    if txt_dest_paht.get() == "":
        msgbox.showwarning("경고","저장경로를 설정하세요")

    #이미지 통합작업
    merge_image()
    
        
#파일 프레임 (추가,삭제 영역)
file_frame = Frame(root)
file_frame.pack(fill="x",padx=5 ,pady=5) #양옆으로 영역 확장

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="추가", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="삭제", command=del_file)
btn_del_file.pack(side="right")

#리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both",padx=5 ,pady=5)

#스크롤바
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

#저장경로 프레임
path_frame = LabelFrame(root, text="저장 경로")
path_frame.pack(fill="x",padx=5 ,pady=5, ipady=5)

txt_dest_paht = Entry(path_frame) #entry
txt_dest_paht.pack(side="left", fill="x", expand=True, ipady=4, padx=5 ,pady=5) #ipady 높이변경

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5 ,pady=5)

#옵션 프레임 (큰 칸 생성)
frame_option = LabelFrame(root, text="옵션") 
frame_option.pack(padx=5 ,pady=5, ipady=5)

#가로넓이 (부속 1)
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left",padx=5 ,pady=5)

#가로넓이 콤보박스
opt_width = ["원본 유지","1024","800","640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left",padx=5 ,pady=5)

#간격
#간격옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left",padx=5 ,pady=5)

#간격옵션 콤보
opt_space = ["없음","좁게","보통","넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left",padx=5 ,pady=5)

#파일 포맷
#파일포맷 옵션 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left",padx=5 ,pady=5)

#파일포맷 콤보
opt_format = ["PNG","JPG","BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left",padx=5 ,pady=5)

#진행상황 프로그래스바
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x",padx=5 ,pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x",padx=5 ,pady=5)

#실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x",padx=5 ,pady=5)

btn_exit = Button(frame_run, text="종료", padx=5, pady=5, width=12, command=root.quit)
btn_exit.pack(side="right",padx=5 ,pady=5)

btn_start = Button(frame_run, text="시작", padx=5, pady=5, width=12, command=start)
btn_start.pack(side="right",padx=5 ,pady=5)


root.resizable(False, False)
root.mainloop()
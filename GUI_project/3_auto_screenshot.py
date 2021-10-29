import time
from PIL import ImageGrab #python image library ,  pip install Pillow 필요

time.sleep(5) #t사용자가 5초대기

for i in range(1,11): #2초 간격을 ㅗ10개 저장
    img = ImageGrab.grab() #현재 스크린 이미지를 저장
    img.save("image{}.png".format(i)) #파일로 저장
    time.sleep(2) #2초 단위




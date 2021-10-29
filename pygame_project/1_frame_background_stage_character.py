import pygame
import os

pygame.init() #초기화 반드시 필요

#화면 크기설정
screen_width = 640 #가로
screen_height = 480 #세로
screen = pygame.display.set_mode((screen_width,screen_height)) #(가로 , 세로)

#화면 타이틀 
pygame.display.set_caption("Pang") 

#FPS
clock = pygame.time.Clock()


#1. 사용자 게임 초기화(배경화면 , 게임 이미지 ,좌표 , 폰트, 속도)
current_path = os.path.dirname(__file__) #현재 파일의 위치 반환
image_path = os.path.join(current_path,"images") # images 폴더 위치 반환

#배경 만들기
background = pygame.image.load(os.path.join(image_path,"background.png"))

#스테이지 만들기
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]
stage_width = stage_size[0]

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path,"character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_hight = character_size[1]
character_X_pos = (screen_width / 2) - (character_width / 2)
character_Y_pos = (screen_height - character_hight - stage_height)

#이벤트 루프
running = True #게임이 진행
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정


    #2 이벤트 처리 구간
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False


    #3. 게임 캐릭터 위치 정의
    

    #4 충돌 처리
   

    #5 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(stage,(0,screen_height - stage_height))
    screen.blit(character,(character_X_pos,character_Y_pos))
    pygame.display.update() #화면을 계속 그리기 , 항상 호출


#게임이 종료
pygame.quit()

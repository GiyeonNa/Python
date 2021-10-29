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
character_speed = 0.3

#이동 방향
to_X = 0

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path,"weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_hight = weapon_size[1]
weapon_speed = 10

#무기 다수 발포 가능
weapons = []


#이벤트 루프
running = True #게임이 진행
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

    #2 이벤트 처리 구간
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                to_X += character_speed
            elif event.key == pygame.K_LEFT:
                to_X -= character_speed
            elif event.key == pygame.K_SPACE:
                weapon_X_pos = character_X_pos + (character_width / 2) - (weapon_width /2)
                weapon_Y_pos = character_Y_pos
                weapons.append([weapon_X_pos,weapon_Y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_X = 0

     #3. 게임 캐릭터 위치 정의
    character_X_pos += to_X * dt

    if character_X_pos < 0:
        character_X_pos = 0
    elif character_X_pos > screen_width - character_width:
        character_X_pos = screen_width -character_width


    #무기 위치 
    #x축은 고정 , y축은 감소하여 위로 올라가야함
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]
    #무기위치를 위로 올린다

    #무기가 천장에 도착
    #w[1] = y좌표, y좌표가 0보다 큰것 -> 천장에 도착하지 않은것만 리스트에 넣음
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
    

    #4 충돌 처리
   

    #5 화면에 그리기
    screen.blit(background,(0,0))
    for weapon_x , weapon_y in weapons:
        screen.blit(weapon,(weapon_x,weapon_y))
    screen.blit(stage,(0,screen_height - stage_height))
    
    screen.blit(character,(character_X_pos,character_Y_pos))
    
    pygame.display.update() #화면을 계속 그리기 , 항상 호출

   

#게임이 종료
pygame.quit()

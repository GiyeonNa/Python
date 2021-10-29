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

#공 만들기 (4개 크기에 대해 따로 처리)
ball_image = [
    pygame.image.load(os.path.join(image_path, "ballon1.png")),
    pygame.image.load(os.path.join(image_path, "ballon2.png")),
    pygame.image.load(os.path.join(image_path, "ballon3.png")),
    pygame.image.load(os.path.join(image_path, "ballon4.png"))
]

#공에 따른 최초 스피드
ball_speed_y = [-18 ,-15 ,-12 ,-9] #index 0 1 2 3 ,올라갈때는 - 로 설정해야함

#공
balls = []

#최초 발생하는 공 정보
balls.append({
    "pos_x" : 50, #공의 X좌표
    "pos_y" : 50, #공의 y좌표
    "img_idx" : 0, #공의 크기
    "to_x" : 3, #공의 x축 이동 방향 - 이면 왼 +이면 오른
    "to_y" : -6, #y축 이동 방향
    "init_spd_y" : ball_speed_y[0]#y 최초 속도 
})

#사라질 무기, 공 정보
weapon_to_remove = -1
ball_to_remove = -1



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
    
    #공 위치 정의
    #enumerate : balls리스트의 n번째 인덱스 값 과 그때 인덱스의 값을 출력 
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_image[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #공이 가로벽에 닿았을때 이동하는 조건
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        #공이 세로벽에 닿았을때 이동하는 조건
        if ball_pos_y >= screen_height - stage_height - ball_height:
            #ball_speed_y 의 0 번째 값을 이용
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            #음수라면 위로 향할꺼고 지속적으로 더하면 양수로 들어가면서 아래도 향한다
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]



    #4 충돌 처리
    
    #캐릭터 rect 정보 저장
    character_rect = character.get_rect()
    character_rect.left = character_X_pos
    character_rect.top = character_Y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        #공 rect 정보 업데이트
        ball_rect = ball_image[ball_img_idx].get_rect()
        ball_rect.top = ball_pos_y
        ball_rect.left = ball_pos_x

        #공 , 캐릭터 충돌
        if character_rect.colliderect(ball_rect):
            running = False
            break

        #공 , 무기 충돌
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            weapon_rect = weapon.get_rect()
            weapon_rect.left =  weapon_pos_x
            weapon_rect.top =  weapon_pos_y

            #충돌 체크
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx #해당 무기 없애기
                ball_to_remove = ball_idx #해당 공 없애기
                break

    #충돌된 공 , 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    #5 화면에 그리기
    screen.blit(background,(0,0))
    for weapon_x , weapon_y in weapons:
        screen.blit(weapon,(weapon_x,weapon_y))

    for idx,val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_image[ball_img_idx] ,(ball_pos_x,ball_pos_y))

    screen.blit(stage,(0,screen_height - stage_height))
    
    screen.blit(character,(character_X_pos,character_Y_pos))
    
    pygame.display.update() #화면을 계속 그리기 , 항상 호출

   

#게임이 종료
pygame.quit()

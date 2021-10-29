import pygame

#시작화면 보여조기
def display_start_screen():
    pygame.draw.circle(scree, WHITE, start_button.center, 60, 5)
    #흰색 동그라미, 중심은 start_button의 중심좌표를 따라가고 반지름 60 두께5

#게임 화면 보여주기
def display_game_screen():
    print("GAME START")

#pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True

#초기화
pygame.init()
screen_width = 1280
screen_height = 720
scree = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Memory Game")

#시작 버튼
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120, screen_height - 120)

#색
BLACK =(0, 0, 0)
WHITE = (255, 255, 255)

#게임 시작 여부
start = False

#게임루프 game loop
running = True #실행중인가?
while running:
    click_pos = None
    #이벤트 루프
    for event in pygame.event.get():
        #창이 닫히는 이벤트
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP: #사용자가마우스 클릭했을때
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    #화면 칠하기
    scree.fill(BLACK)

    if start:
        #게임 화면 표시
        display_game_screen()
    else:
        # 시작 화면
        display_start_screen()

    #사용자가 클릭했다면
    if click_pos:
        check_buttons(click_pos)
    
    #화면 업데이트
    pygame.display.update()

#게임 종료
pygame.quit()
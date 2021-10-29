import pygame

#시작화면 보여조기
def display_start_screen():
    pygame.draw.circle(scree, WHITE, start_button.center, 60, 5)
    #흰색 동그라미, 중심은 start_button의 중심좌표를 따라가고 반지름 60 두께5


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

#게임루프 game loop
running = True #실행중인가?
while running:
    #이벤트 루프
    for event in pygame.event.get():
        
        #창이 닫히는 이벤트
        if event.type == pygame.QUIT:
            running = False
    #화면 칠하기
    scree.fill(BLACK)

    # 시작 화면
    display_start_screen()

    #화면 업데이트
    pygame.display.update()

#게임 종료
pygame.quit()
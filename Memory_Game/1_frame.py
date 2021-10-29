import pygame
#초기화
pygame.init()
screen_width = 1280
screen_height = 720
scree = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Memory Game")

#게임루프 game loop
running = True #실행중인가?
while running:
    #이벤트 루프
    for event in pygame.event.get():
        
        #창이 닫히는 이벤트
        if event.type == pygame.QUIT:
            running = False



#게임 종료
pygame.quit()
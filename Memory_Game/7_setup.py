import pygame
from random import *

#레벨에 맞게 설정
def setup(level):
    #얼만동안 숫자를 보여줄지
    global display_time
    display_time = 5 - (level // 3)
    display_time = max(display_time, 1)

    #얼마나 많은 숫자를 보여줄 것인가
    number_count = (level // 3 ) + 5
    #최대수 20으로 고정
    number_count = min(number_count, 20)

    #실제화면에 grid 형식으로 숫재 배치
    shuffle_grid(number_count)

#숫자 섞기
def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130 #각 grid cell 크기
    button_size = 110 # grid cell 에서 그려지 버튼크기
    screen_left_margin = 55 # 전체 스크린 왼쪽여백
    screen_top_margin = 20 # 전체 스크린 위쪽 여백

    grid = [[0 for col in range(columns)] for row in range(rows)] #5 * 9
    
    number = 1 #시작 숫자 1부터 number_count 까지
    while number <= number_count:
        row_idx = randrange(0, rows) #0~4
        col_idx = randrange(0, columns) #0~8

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            #현재 grid cell 위치 기준으로 xy위치 구함
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

            #버튼그리기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center =(center_x, center_y)

            number_buttons.append(button)

    print(grid)

#시작화면 보여조기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)

    msg = game_font.render(f"{curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=start_button.center)

    screen.blit(msg, msg_rect)
    

#게임 화면 보여주기
def display_game_screen():
    global hidden

    if not hidden:
        #현재 흐르는 시간 - 눌렀을때의 시간
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        if elapsed_time > display_time:
            hidden = True

    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            #버튼 사각형
            pygame.draw.rect(screen, WHITE, rect)

        else:
            #숫자 텍스트
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)




#pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start, start_ticks
    #게임ㅇ ㅣ시작해ㅆ다면
    if start:
        check_number_buttons(pos)

    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks()#타이머 시작

def check_number_buttons(pos):
    global hidden, start, curr_level

    for button in number_buttons:
        if button.collidepoint(pos):
            #첫번째랑 같다면
            if button == number_buttons[0]:
                print("correct")
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else: #잘못누름
                game_over()

            break

    #모든 숫자 눌렀을 경우
    if len(number_buttons) == 0:
        start = False
        hidden = False
        curr_level += 1
        setup(curr_level)

#게임 오버
def game_over():
    global running
    running = False

    msg = game_font.render(f"Your level is {curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=(screen_width/2, screen_height/2))

    screen.fill(BLACK)
    screen.blit(msg, msg_rect)

#초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120) #폰트정의

#시작 버튼
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120, screen_height - 120)

#색
BLACK =(0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

#플레이어가 눌러야하는 버튼들
number_buttons = []

#현재 레벨
curr_level = 1 

#숫자를 보여주는 시간
display_time = None

#시간계산
start_ticks = None

#게임 시작 여부
start = False

#숫자 숨김(조건 1) 1을 클릭 , 조건 2) 시간이 경과)
hidden = False

#게임설정
setup(1)

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
    screen.fill(BLACK)

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

pygame.time.delay(5000)

#게임 종료
pygame.quit()
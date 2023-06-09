from logics import get_number_from_index, get_empty_list, get_index_from_number, is_zero_in_mas, pretty_print ,\
    insert_2_or_4, random, move_left, move_right, move_up, move_down, can_move
import pygame
import sys




def draw_interface(score,delta=0): #зробимо delta по заумовчанню, бо ми його не всюди приймаємо
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont('strxingkai', 70)
    font_score = pygame.font.SysFont('simsun', 48)
    font_delta = pygame.font.SysFont('simsun', 32)
    text_score = font_score.render('Score: ', True, COLOR_TEXT)
    text_score_value = font_score.render(f'{score}', True, COLOR_TEXT)
    screen.blit(text_score, (20,35))
    screen.blit(text_score_value, (175,35))
    # тут додамо перевірку, щоб коли за рух не схлопувались жодні блоки, не виводився цей текст
    if delta>0:
        text_delta = font_delta.render(f'+{delta}', True, COLOR_TEXT)
        screen.blit(text_delta, (170,65))
    pretty_print(mas)
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column*SIZE_BLOCK+(column+1)*MARGIN
            h = row*SIZE_BLOCK+(row+1)*MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w,h,SIZE_BLOCK,SIZE_BLOCK))
            if value!=0:
                font_w, font_h = text.get_size()
                text_x = w+(SIZE_BLOCK-font_w) / 2
                text_y = h+(SIZE_BLOCK-font_h) / 2
                screen.blit(text, (text_x, text_y))




COLOR_TEXT = (255,127,0)
COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 230, 128),
    8: (255, 255, 0),
    16: (255, 195, 255),
    32: (255, 128, 128),
    64: (255, 154, 0),
    128: (255, 128, 0),
    256: (204, 102, 0),
    512: (255, 64, 64),
    1024: (255, 102, 178),
    2048: (102, 0, 51),
}


mas = [
	[0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]


WHITE = (255, 255, 255)
GRAY = (130,130,130)
BLACK = (0,0,0)




BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10 
WIDTH = BLOCKS*SIZE_BLOCK+(BLOCKS+1)*MARGIN
HEIGHT = WIDTH+110


TITLE_REC = pygame.Rect(0,0, WIDTH, 110)
score = 0

mas[1][2] = 2
mas[3][0] = 4
print(get_empty_list(mas))
pretty_print(mas)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')


draw_interface(score)# тут delta додавати не будемо, бо тут вона буде рівна 0
pygame.display.update()
while is_zero_in_mas(mas) or can_move(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            delta = 0
            # відповідно будемо виводити тепер ще одну змінну
            if event.key == pygame.K_LEFT:
                mas, delta = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas, delta = move_right(mas)
            elif event.key == pygame.K_UP:
                mas, delta = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas, delta = move_down(mas)
            score += delta
            empty = get_empty_list(mas)
            random.shuffle(empty)
            random_num = empty.pop()
            x, y = get_index_from_number(random_num)
            mas = insert_2_or_4(mas, x, y)  
            print(f'Ми заповнили елемент під номером {random_num}')
            draw_interface(score, delta) # а ось сюди додамо
            pygame.display.update()
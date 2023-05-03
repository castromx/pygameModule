from logics import get_number_from_index, get_empty_list, get_index_from_number, is_zero_in_mas, pretty_print ,\
    insert_2_or_4, random, move_left, move_right, move_up, move_down, can_move
import pygame
import sys
from database import get_best, cur, inster_result
import json
import os.path


GAMERS_DB = get_best()



def draw_top_gamers():
    font_top = pygame.font.SysFont('simsun', 30)
    font_gamer = pygame.font.SysFont('Arial', 24)
    text_head = font_top.render('Best tries: ', True, COLOR_TEXT)
    screen.blit(text_head, (270, 5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f'{index+1}. {name} - {score}'
        text_gamer = font_gamer.render(s, True, COLOR_TEXT)
        screen.blit(text_gamer, (270, 30 + 25*index))
        print(index, gamer)

def draw_interface(score,delta=0): 
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont('strxingkai', 70)
    font_score = pygame.font.SysFont('simsun', 48)
    font_delta = pygame.font.SysFont('simsun', 32)
    text_score = font_score.render('Score: ', True, COLOR_TEXT)
    text_score_value = font_score.render(f'{score}', True, COLOR_TEXT)
    screen.blit(text_score, (20,35))
    screen.blit(text_score_value, (175,35))
    if delta>0:
        text_delta = font_delta.render(f'+{delta}', True, COLOR_TEXT)
        screen.blit(text_delta, (170,65))
    pretty_print(mas)
    draw_top_gamers()
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




WHITE = (255, 255, 255)
GRAY = (130,130,130)
BLACK = (0,0,0)




BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10 
WIDTH = BLOCKS*SIZE_BLOCK+(BLOCKS+1)*MARGIN
HEIGHT = WIDTH+110


TITLE_REC = pygame.Rect(0,0, WIDTH, 110)



def init_mas_score():
    global score, mas
    mas = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_num1 = empty.pop()
    random_num2 = empty.pop()
    x1, y1 = get_index_from_number(random_num1)
    mas = insert_2_or_4(mas, x1, y1)
    x2, y2 = get_index_from_number(random_num2)
    mas = insert_2_or_4(mas, x2, y2)
    score = 0


mas = None
score = None
USERNAME = None
path = os.getcwd()
if 'data.txt' in os.listdir():
    with open('data.txt') as file:
        data = json.load(file)
        mas = data['mas']
        score = data['score']
        USERNAME = data['user']
    full_path = os.path.join(path, 'data.txt')
    os.remove(full_path)
else:
    init_mas_score()

print(get_empty_list(mas))
pretty_print(mas)




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')



def draw_intro():
    img2048 = pygame.image.load('intr2048.png')
    font = pygame.font.SysFont('strxingkai', 70)
    text_welcome = font.render('Welcome!', True, BLACK)
    name = "Введіть ім'я"
    is_find_name = False
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == "Введіть ім'я":
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name)>2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break

        screen.fill(WHITE)
        text_name = font.render(name, True, BLACK)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(img2048, [10,10])
        screen.blit(text_welcome, (230,60))
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)


def draw_game_over():
    global USERNAME, mas, score, GAMERS_DB
    img2048 = pygame.image.load('intr2048.png')
    font = pygame.font.SysFont('strxingkai', 65)
    font_kn = pygame.font.SysFont('strxingkai', 30)
    text_game_over = font.render('Game over!', True, BLACK)
    text_score = font.render(f'Ви набрали {score}', True, BLACK)
    best_score = GAMERS_DB[0][1]
    text_kn1 = font_kn.render("Пробіл - почати грати з тим же іменем", True, COLOR_TEXT)
    text_kn2 = font_kn.render("Enter - Ввести нове ім'я", True, COLOR_TEXT)
    if score > best_score:
        text = 'Рекорд побитий'
    else:
        text = f'Рекорд {best_score}'
    text_record = font.render(text, True, BLACK)
    inster_result(USERNAME, score)
    GAMERS_DB = get_best()
    make_desicion = False
    while not make_desicion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    make_desicion = True
                    init_mas_score()
                elif event.key == pygame.K_RETURN:
                    USERNAME = None
                    make_desicion = True
                    init_mas_score()
        screen.fill(WHITE)
        screen.blit(text_game_over, (220,80))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(img2048, [10,10])
        screen.blit(text_kn1, (30, 390))
        screen.blit(text_kn2, (30, 430))
        pygame.display.update()
    screen.fill(BLACK)


def save_game():
    data = {
        'user': USERNAME,
        'score': score,
        'mas': mas
    }
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)



def game_loop():
    global score, mas
    draw_interface(score)
    pygame.display.update()
    is_mas_move = True
    while is_zero_in_mas(mas) or can_move(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game()
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT:
                    mas, delta, is_mas_move = move_left(mas)
                elif event.key == pygame.K_RIGHT:
                    mas, delta, is_mas_move = move_right(mas)
                elif event.key == pygame.K_UP:
                    mas, delta, is_mas_move = move_up(mas)
                elif event.key == pygame.K_DOWN:
                    mas, delta, is_mas_move = move_down(mas)
                score += delta
                if is_zero_in_mas(mas) and is_mas_move:
                    empty = get_empty_list(mas)
                    random.shuffle(empty)
                    random_num = empty.pop()
                    x, y = get_index_from_number(random_num)
                    mas = insert_2_or_4(mas, x, y)  
                    print(f'Ми заповнили елемент під номером {random_num}')
                    is_mas_move = False
                draw_interface(score, delta)
                pygame.display.update()


while True:
    if USERNAME is None:
        draw_intro()
    game_loop()
    draw_game_over()
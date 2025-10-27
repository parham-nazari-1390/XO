
import pygame
import math

pygame.init()

WIDTH = 480
HEIGHT=480
ROWS = 3
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

CAT_IMAGE = pygame.transform.scale(pygame.image.load("x.png"), (150, 150))

MOUSE_IMAGE = pygame.transform.scale(pygame.image.load("o.png"), (150, 150))



END_FONT = pygame.font.SysFont('arial', 40)

def draw_grid():
    gap = WIDTH // ROWS

    x = 0
    y = 0

    for i in range(ROWS):
        x = i * gap
        pygame.draw.line(SCREEN, GRAY, (x, 0), (x, WIDTH), 3)
        pygame.draw.line(SCREEN, GRAY, (0, x), (WIDTH, x), 3)


def initialize_grid():
    dis_to_center = WIDTH // ROWS // 2

    game_array = [[None, None, None], [None, None, None], [None, None, None]]

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x = dis_to_center * (2 * j + 1)
            y = dis_to_center * (2 * i + 1)

            game_array[i][j] = (x, y,"", True)

    return game_array


def click(game_array):
    global cat_turn, mouse_turn, images

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char, can_play = game_array[i][j]

            dis = math.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)

            if dis < WIDTH // ROWS // 2 and can_play:
                if cat_turn:  
                    images.append((x, y, CAT_IMAGE))
                    cat_turn = False
                    mouse_turn = True
                    game_array[i][j] = (x, y, 'x', False)

                elif mouse_turn:  
                    images.append((x, y, MOUSE_IMAGE))
                    cat_turn = True
                    mouse_turn = False
                    game_array[i][j] = (x, y, 'o', False)


def has_won(game_array):
    for row in range(len(game_array)):
        if (game_array[row][0][2] == game_array[row][1][2] == game_array[row][2][2]) and game_array[row][0][2] != "":
            display_message(game_array[row][0][2].upper() + "  Win")
            return True

    for col in range(len(game_array)):
        if (game_array[0][col][2] == game_array[1][col][2] == game_array[2][col][2]) and game_array[0][col][2] != "":
            display_message(game_array[0][col][2].upper() + "  Win")
            return True

    if (game_array[0][0][2] == game_array[1][1][2] == game_array[2][2][2]) and game_array[0][0][2] != "":
        display_message(game_array[0][0][2].upper() + "  Won")
        return True

    if (game_array[0][2][2] == game_array[1][1][2] == game_array[2][0][2]) and game_array[0][2][2] != "":
        display_message(game_array[0][2][2].upper() + "  Won")
        return True

    return False


def has_drawn(game_array):
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            if game_array[i][j][2] == "":
                return False

    display_message("It's a tie!")
    return True


def display_message(content):
    pygame.time.delay(500)
    SCREEN.fill(WHITE)
    end_text = END_FONT.render(content, 1, BLACK)
    SCREEN.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)


def render():
    SCREEN.fill(WHITE)
    draw_grid()

    for image in images:
        x, y, IMAGE = image
        SCREEN.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

    pygame.display.update()


def main():
    global cat_turn, mouse_turn, images, draw

    images = []
    draw = False

    run = True

    cat_turn = True
    mouse_turn = False

    game_array = initialize_grid()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(game_array)

        render()

        if has_won(game_array) or has_drawn(game_array):
            run = False

while True:
    if __name__ == '__main__':
        main()

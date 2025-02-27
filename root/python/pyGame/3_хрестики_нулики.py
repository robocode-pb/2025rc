import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Налаштування екрану
WIN_LENGTH = 3 # <= BOARD_SIZE !!!!!
BOARD_SIZE = 3
CELL_SIZE = 100
WIDTH = CELL_SIZE * BOARD_SIZE
HEIGHT = WIDTH + 100
LINE_WIDTH = 5
GRID_COLOR = (200, 200, 200)
X_COLOR = (0, 0, 255)
O_COLOR = (255, 0, 0)
BG_COLOR = (20, 20, 20)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER_COLOR = (100, 100, 100)

FONT = pygame.font.Font(None, 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Хрестики-нулики")
screen.fill(BG_COLOR)

# Гра

board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
current_player = "X"
game_over = False
winner = None

# Малювання сітки
def draw_grid():
    for x in range(1, BOARD_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x * CELL_SIZE, 50), (x * CELL_SIZE, HEIGHT - 50), LINE_WIDTH)
        pygame.draw.line(screen, GRID_COLOR, (0, x * CELL_SIZE + 50), (WIDTH, x * CELL_SIZE + 50), LINE_WIDTH)

# Малювання символу
def draw_symbol(row, col, symbol):
    center_x = col * CELL_SIZE + CELL_SIZE // 2
    center_y = row * CELL_SIZE + CELL_SIZE // 2 + 50
    if symbol == "X":
        pygame.draw.line(screen, X_COLOR, 
                         (center_x - CELL_SIZE // 4, center_y - CELL_SIZE // 4), 
                         (center_x + CELL_SIZE // 4, center_y + CELL_SIZE // 4), LINE_WIDTH)
        pygame.draw.line(screen, X_COLOR, 
                         (center_x + CELL_SIZE // 4, center_y - CELL_SIZE // 4), 
                         (center_x - CELL_SIZE // 4, center_y + CELL_SIZE // 4), LINE_WIDTH)
    elif symbol == "O":
        pygame.draw.circle(screen, O_COLOR, (center_x, center_y), CELL_SIZE // 4, LINE_WIDTH)

# Перевірка переможця
def check_winner():
    # Перевірка рядків
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE - WIN_LENGTH + 1): 
            if board[row][col] != "" and all(board[row][col + i] == board[row][col] for i in range(WIN_LENGTH)):
                return board[row][col]

    # Перевірка стовпців
    for col in range(BOARD_SIZE):
        for row in range(BOARD_SIZE - WIN_LENGTH + 1):
            if board[row][col] != "" and all(board[row + i][col] == board[row][col] for i in range(WIN_LENGTH)):
                return board[row][col]

    # Перевірка головних діагоналей
    for row in range(BOARD_SIZE - WIN_LENGTH + 1):
        for col in range(BOARD_SIZE - WIN_LENGTH + 1):
            if board[row][col] != "" and all(board[row + i][col + i] == board[row][col] for i in range(WIN_LENGTH)):
                return board[row][col]

    # Перевірка побічних діагоналей
    for row in range(BOARD_SIZE - WIN_LENGTH + 1):
        for col in range(WIN_LENGTH - 1, BOARD_SIZE):
            if board[row][col] != "" and all(board[row + i][col - i] == board[row][col] for i in range(WIN_LENGTH)):
                return board[row][col]

    # Перевірка на нічию (немає порожніх клітинок)
    if all(cell != "" for row in board for cell in row):
        return "Нічия"

    return None


# Відображення тексту
def draw_text(text, y, color=TEXT_COLOR):
    label = FONT.render(text, True, color)
    text_rect = label.get_rect(center=(WIDTH // 2, y))
    screen.blit(label, text_rect)

# Відображення кнопки
def draw_button():
    mouse_pos = pygame.mouse.get_pos()
    button_rect = pygame.Rect(WIDTH/2-100, HEIGHT - 40, 200, 30)
    color = BUTTON_HOVER_COLOR if button_rect.collidepoint(mouse_pos) else BUTTON_COLOR
    pygame.draw.rect(screen, color, button_rect)
    draw_text("Перезапустити", HEIGHT - 25, TEXT_COLOR)
    return button_rect

# Перезапуск гри
def restart_game():
    global board, current_player, game_over, winner
    board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = "X"
    game_over = False
    winner = None
    screen.fill(BG_COLOR)

# Головний цикл гри
while True:
    screen.fill(BG_COLOR)
    draw_grid()
    
    # Відображення стану гри
    if game_over:
        draw_text(f"Переможець: {check_winner()}", 25)
    else:
        draw_text(f"Хід: {current_player}", 25)
    
    # Малювання символів
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            draw_symbol(row, col, board[row][col])

    # Кнопка "Перезапустити"
    button_reset = draw_button()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_reset.collidepoint(event.pos):
                restart_game()

            if not winner: 
                mouse_x, mouse_y = event.pos
                if mouse_y > 50 and mouse_y < HEIGHT - 50:
                    row, col = (mouse_y - 50) // CELL_SIZE, mouse_x // CELL_SIZE
                    if board[row][col] == "":
                        board[row][col] = current_player
                        winner = check_winner()
                        if winner:
                            game_over = True
                        current_player = "O" if current_player == "X" else "X"

    pygame.display.flip()
    pygame.time.Clock().tick(30)

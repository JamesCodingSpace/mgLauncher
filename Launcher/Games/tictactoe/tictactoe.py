import pygame
import random

# Initialisierung von Pygame
pygame.init()

# Fenstergröße und Titel
WIDTH, HEIGHT = 300, 350
TITLE = "Tic Tac Toe"
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Farben
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Spielvariablen
FPS = 60
CELL_SIZE = WIDTH // 3
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False
mode = None

# Funktion zum Zeichnen des Spielfelds
def draw_board():
    WIN.fill(WHITE)
    # Zeichne horizontale Linien
    for i in range(1, 3):
        pygame.draw.line(WIN, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 3)
    # Zeichne vertikale Linien
    for i in range(1, 3):
        pygame.draw.line(WIN, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT - 50), 3)

# Funktion zum Zeichnen der Spielsteine
def draw_symbols():
    for row in range(3):
        for col in range(3):
            symbol = board[row][col]
            if symbol != " ":
                font = pygame.font.SysFont(None, 100)
                text = font.render(symbol, True, BLACK)
                text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                WIN.blit(text, text_rect)

# Funktion zum Überprüfen auf Gewinner
def check_winner(board, player):
    # Überprüfe horizontale und vertikale Linien
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # Überprüfe diagonale Linien
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Funktion zum Überprüfen auf Unentschieden
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Funktion zum setzen eines Zuges für den Computer (Minimax Algorithmus)
def computer_move():
    best_score = float("-inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    board[best_move[0]][best_move[1]] = "O"

def minimax(board, maximizing):
    if check_winner(board, "X"):
        return -1
    elif check_winner(board, "O"):
        return 1
    elif check_draw(board):
        return 0

    if maximizing:
        best_score = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# Funktion zur Auswahl des Spielmodus
def choose_mode():
    global mode
    font = pygame.font.SysFont(None, 40)
    singleplayer_text = font.render("Einzelspieler", True, BLACK)
    multiplayer_text = font.render("Mehrspieler", True, BLACK)
    singleplayer_rect = singleplayer_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    multiplayer_rect = multiplayer_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 30))
    while mode is None:
        WIN.fill(WHITE)
        WIN.blit(singleplayer_text, singleplayer_rect)
        WIN.blit(multiplayer_text, multiplayer_rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if singleplayer_rect.collidepoint(x, y):
                    mode = "singleplayer"
                elif multiplayer_rect.collidepoint(x, y):
                    mode = "multiplayer"

choose_mode()

# Hauptspiel-Schleife
clock = pygame.time.Clock()
running = True
winner = None
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and current_player == "X":
            x, y = pygame.mouse.get_pos()
            row, col = y // CELL_SIZE, x // CELL_SIZE
            if board[row][col] == " ":
                board[row][col] = "X"
                if check_winner(board, "X"):
                    winner = "X"
                    game_over = True
                elif check_draw(board):
                    winner = "Draw"
                    game_over = True
                else:
                    current_player = "O"
        elif not game_over and current_player == "O" and mode == "singleplayer":
            computer_move()
            if check_winner(board, "O"):
                winner = "O"
                game_over = True
            elif check_draw(board):
                winner = "Draw"
                game_over = True
            else:
                current_player = "X"
        elif not game_over and current_player == "O" and mode == "multiplayer":
            x, y = pygame.mouse.get_pos()
            row, col = y // CELL_SIZE, x // CELL_SIZE
            if board[row][col] == " ":
                board[row][col] = "O"
                if check_winner(board, "O"):
                    winner = "O"
                    game_over = True
                elif check_draw(board):
                    winner = "Draw"
                    game_over = True
                else:
                    current_player = "X"

    draw_board()
    draw_symbols()
    if game_over:
        font = pygame.font.SysFont(None, 50)
        if winner == "Draw":
            text = font.render("It's a draw!", True, BLACK)
        else:
            text = font.render(f"Player {winner} wins!", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 25))
        WIN.blit(text, text_rect)
        reset_button = pygame.Rect(0, HEIGHT - 50, WIDTH, 50)
        pygame.draw.rect(WIN, GRAY, reset_button)
        reset_font = pygame.font.SysFont(None, 30)
        reset_text = reset_font.render("Neustart", True, BLACK)
        reset_text_rect = reset_text.get_rect(center=reset_button.center)
        WIN.blit(reset_text, reset_text_rect)
    pygame.display.update()

    if game_over:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_button.collidepoint(event.pos):
                    board = [[" " for _ in range(3)] for _ in range(3)]
                    current_player = "X"
                    game_over = False
                    winner = None

pygame.quit()

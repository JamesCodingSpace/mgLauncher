import pygame
import random

# Konstanten für das Spielfeld
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(0, 255, 255), (255, 0, 255), (255, 255, 0), (0, 255, 0), (255, 165, 0), (255, 0, 0), (0, 0, 255)]

# Definition der Tetriminos
tetriminos = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # J
    [[1, 1, 1], [0, 0, 1]],  # L
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_tetrimino = self.new_tetrimino()
        self.x = GRID_WIDTH // 2 - len(self.current_tetrimino[0]) // 2
        self.y = 0
        self.score = 0
        self.game_over = False

    def new_tetrimino(self):
        return random.choice(tetriminos)

    def draw_block(self, x, y, color):
        pygame.draw.rect(self.screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_grid(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    self.draw_block(x, y, COLORS[cell - 1])

    def draw_tetrimino(self):
        for y, row in enumerate(self.current_tetrimino):
            for x, cell in enumerate(row):
                if cell:
                    self.draw_block(x + self.x, y + self.y, COLORS[cell - 1])

    def check_collision(self):
        for y, row in enumerate(self.current_tetrimino):
            for x, cell in enumerate(row):
                if cell and (self.grid[y + self.y][x + self.x] or x + self.x < 0 or x + self.x >= GRID_WIDTH or y + self.y >= GRID_HEIGHT):
                    return True
        return False

    def merge_tetrimino(self):
        for y, row in enumerate(self.current_tetrimino):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[y + self.y][x + self.x] = cell
        self.clear_lines()

    def clear_lines(self):
        lines_cleared = 0
        for y, row in enumerate(self.grid[:-1]):
            if all(row):
                del self.grid[y]
                self.grid.insert(0, [0] * GRID_WIDTH)
                lines_cleared += 1
        self.score += lines_cleared ** 2

    def run(self):
        while not self.game_over:
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x -= 1
                        if self.check_collision():
                            self.x += 1
                    elif event.key == pygame.K_RIGHT:
                        self.x += 1
                        if self.check_collision():
                            self.x -= 1
                    elif event.key == pygame.K_DOWN:
                        self.y += 1
                        if self.check_collision():
                            self.y -= 1
                    elif event.key == pygame.K_UP:
                        self.current_tetrimino = list(zip(*self.current_tetrimino[::-1]))
                        if self.check_collision():
                            self.current_tetrimino = list(zip(*self.current_tetrimino[::-1]))

            self.y += 1
            if self.check_collision():
                self.y -= 1
                self.merge_tetrimino()
                self.current_tetrimino = self.new_tetrimino()
                self.x = GRID_WIDTH // 2 - len(self.current_tetrimino[0]) // 2
                self.y = 0
                if self.check_collision():
                    self.game_over = True

            self.draw_grid()
            self.draw_tetrimino()
            pygame.display.flip()
            self.clock.tick(5)

        pygame.quit()

if __name__ == "__main__":
    game = Tetris()
    game.run()

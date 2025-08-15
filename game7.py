import random
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLOCK_SIZE = 100
GRID_SIZE = 5
MARGIN = 10

# Colors
COLORS = {
    'red': (255, 0, 0),
    'blue': (0, 0, 255),
    'green': (0, 255, 0),
    'yellow': (255, 255, 0),
    'purple': (128, 0, 128)
}

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Blockbusters 3D-Style')

class BlockbustersGame:
    def __init__(self):
        self.grid = self.initialize_grid()
        self.score = 0
        self.selected_block = None

    def initialize_grid(self):
        # Create a 5x5 grid with random colors
        grid = []
        for _ in range(GRID_SIZE):
            row = [random.choice(list(COLORS.keys())) for _ in range(GRID_SIZE)]
            grid.append(row)
        return grid

    def display_grid(self):
        screen.fill((0, 0, 0))  # Clear screen
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                color = COLORS[self.grid[i][j]]
                # Draw 3D-style block
                self.draw_3d_block(j * BLOCK_SIZE + MARGIN, i * BLOCK_SIZE + MARGIN, color)
        pygame.display.flip()

    def draw_3d_block(self, x, y, color):
        # Draw a simple 3D-style block
        pygame.draw.polygon(screen, color, [(x, y), (x + BLOCK_SIZE, y), (x + BLOCK_SIZE - 20, y + BLOCK_SIZE), (x - 20, y + BLOCK_SIZE)])

    def get_block_position(self, pos):
        x, y = pos
        grid_x = x // BLOCK_SIZE
        grid_y = y // BLOCK_SIZE
        if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
            return grid_x, grid_y
        return None

    def swap_blocks(self, x1, y1, x2, y2):
        # Swap two adjacent blocks
        if abs(x1 - x2) + abs(y1 - y2) == 1:
            self.grid[x1][y1], self.grid[x2][y2] = self.grid[x2][y2], self.grid[x1][y1]
            self.check_and_clear_matches()

    def check_and_clear_matches(self):
        # Check for matches and clear them
        # This is a simplified version and should be expanded for full functionality
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.check_match(i, j):
                    self.clear_match(i, j)
                    self.update_grid()

    def check_match(self, x, y):
        # Check for matches of three or more in horizontal and vertical directions
        # Return True if a match is found
        color = self.grid[x][y]
        if x + 2 < GRID_SIZE and self.grid[x+1][y] == color and self.grid[x+2][y] == color:
            return True
        if y + 2 < GRID_SIZE and self.grid[x][y+1] == color and self.grid[x][y+2] == color:
            return True
        return False

    def clear_match(self, x, y):
        # Clear the matched blocks and update the score
        color = self.grid[x][y]
        if x + 2 < GRID_SIZE and self.grid[x+1][y] == color and self.grid[x+2][y] == color:
            self.grid[x][y] = self.grid[x+1][y] = self.grid[x+2][y] = None
            self.score += 3
        if y + 2 < GRID_SIZE and self.grid[x][y+1] == color and self.grid[x][y+2] == color:
            self.grid[x][y] = self.grid[x][y+1] = self.grid[x][y+2] = None
            self.score += 3

    def update_grid(self):
        # Move blocks down to fill gaps and add new blocks from the top
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] is None:
                    for k in range(i, 0, -1):
                        self.grid[k][j] = self.grid[k-1][j]
                    self.grid[0][j] = random.choice(list(COLORS.keys()))

    def play(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    block_pos = self.get_block_position(pos)
                    if block_pos:
                        if self.selected_block:
                            self.swap_blocks(self.selected_block[0], self.selected_block[1], block_pos[0], block_pos[1])
                            self.selected_block = None
                        else:
                            self.selected_block = block_pos
            self.display_grid()
            clock.tick(60)
        pygame.quit()
        sys.exit()

# Start the game
game = BlockbustersGame()
game.play()
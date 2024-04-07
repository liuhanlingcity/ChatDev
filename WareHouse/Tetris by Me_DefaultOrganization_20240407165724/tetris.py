'''
This file contains the Tetris class which represents the game logic and handles user input.
'''
import pygame
from piece import Piece
class Tetris:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.grid = [[0] * 10 for _ in range(20)]
        self.current_piece = None
        self.next_piece = None
        self.score = 0
    def run(self):
        '''
        Runs the game loop.
        '''
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
    def update(self):
        '''
        Updates the game state.
        '''
        self.move_piece(0, 1)
        if self.check_collision():
            self.move_piece(0, -1)
            self.place_piece()
            self.clear_lines()
            self.generate_piece()
    def draw(self):
        '''
        Draws the game screen.
        '''
        self.screen.fill((0, 0, 0))
        self.draw_grid()
        self.draw_piece()
        self.draw_next_piece()
    def move_piece(self, dx, dy):
        '''
        Moves the current piece by the specified amount.
        '''
        if self.current_piece is not None:
            new_x = self.current_piece.x + dx
            new_y = self.current_piece.y + dy
            if self.is_valid_move(new_x, new_y, self.current_piece.shape):
                self.current_piece.x = new_x
                self.current_piece.y = new_y
    def rotate_piece(self):
        '''
        Rotates the current piece.
        '''
        if self.current_piece is not None:
            rotated_shape = self.current_piece.rotate()
            if self.is_valid_move(self.current_piece.x, self.current_piece.y, rotated_shape):
                self.current_piece.shape = rotated_shape
    def drop_piece(self):
        '''
        Drops the current piece to the bottom of the grid.
        '''
        if self.current_piece is not None:
            while self.is_valid_move(self.current_piece.x, self.current_piece.y + 1, self.current_piece.shape):
                self.current_piece.y += 1
    def check_collision(self):
        '''
        Checks if the current piece collides with the grid or other pieces.
        '''
        if self.current_piece is not None:
            for y in range(len(self.current_piece.shape)):
                for x in range(len(self.current_piece.shape[y])):
                    if self.current_piece.shape[y][x] != 0:
                        grid_x = self.current_piece.x + x
                        grid_y = self.current_piece.y + y
                        if grid_y >= len(self.grid) or grid_x < 0 or grid_x >= len(self.grid[0]) or self.grid[grid_y][grid_x] != 0:
                            return True
        return False
    def clear_lines(self):
        '''
        Clears completed lines from the grid and updates the score.
        '''
        lines_cleared = 0
        for y in range(len(self.grid)):
            if all(cell != 0 for cell in self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [0] * 10)
                lines_cleared += 1
        self.score += lines_cleared ** 2
    def generate_piece(self):
        '''
        Generates a new current piece and next piece.
        '''
        self.current_piece = self.next_piece
        self.next_piece = Piece()
        if self.check_collision():
            self.current_piece = None
            self.next_piece = None
            self.score = 0
    def draw_grid(self):
        '''
        Draws the grid on the screen.
        '''
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                cell = self.grid[y][x]
                if cell != 0:
                    pygame.draw.rect(self.screen, (255, 255, 255), (x * 40, y * 40, 40, 40))
    def draw_piece(self):
        '''
        Draws the current piece on the screen.
        '''
        if self.current_piece is not None:
            for y in range(len(self.current_piece.shape)):
                for x in range(len(self.current_piece.shape[y])):
                    if self.current_piece.shape[y][x] != 0:
                        grid_x = self.current_piece.x + x
                        grid_y = self.current_piece.y + y
                        pygame.draw.rect(self.screen, (255, 255, 255), (grid_x * 40, grid_y * 40, 40, 40))
    def draw_next_piece(self):
        '''
        Draws the next piece on the screen.
        '''
        if self.next_piece is not None:
            for y in range(len(self.next_piece.shape)):
                for x in range(len(self.next_piece.shape[y])):
                    if self.next_piece.shape[y][x] != 0:
                        grid_x = x + 11
                        grid_y = y + 1
                        pygame.draw.rect(self.screen, (255, 255, 255), (grid_x * 40, grid_y * 40, 40, 40))
    def is_valid_move(self, x, y, shape):
        '''
        Checks if a move is valid for the current piece.
        '''
        for row in range(len(shape)):
            for col in range(len(shape[row])):
                if shape[row][col] != 0:
                    grid_x = x + col
                    grid_y = y + row
                    if grid_y >= len(self.grid) or grid_x < 0 or grid_x >= len(self.grid[0]) or self.grid[grid_y][grid_x] != 0:
                        return False
        return True
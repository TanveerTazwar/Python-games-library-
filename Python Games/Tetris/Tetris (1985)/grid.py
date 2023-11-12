import pygame
from colors import Colors
class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 40
        self.grid = [[0 for j in range(self.num_cols)]for i in range(self.num_rows+2)]  # This line is called a list
        self.colors = Colors.get_cell_colors()
        # comprehension
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")
            print()
    def is_inside(self, row, column):
        if row>=0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        else:
            return False
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0
    def move_row_down(self,row, num_rows):
        for column in range(self.num_cols):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0
    def clear_full_rows(self):
        completed = 0
        for row in range(self.num_rows -1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed+=1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0
    def draw(self, screen):
        pygame.font.init()
        title_font = pygame.font.Font(None, 30)
        title_font2 = pygame.font.Font("Minecraft.ttf", 40)
        begin_surface = title_font2.render("<!", True, Colors.RusGreen)
        end_surface = title_font2.render("!>", True, Colors.RusGreen)
        dot = title_font.render(".", True, Colors.RusGreen)
        ender = title_font2.render("=", True, Colors.RusGreen)
        a = title_font2.render("\\/", True, Colors.RusGreen)
        b = title_font2.render("\\/", True, Colors.RusGreen)
        for row in range(self.num_rows+2):
            for column in range(self.num_cols):
                if row<21:
                    if column == 0:
                        screen.blit(begin_surface, (column*self.cell_size, row*self.cell_size +16, 50, 50))
                    if column == self.num_cols-1:
                        screen.blit(end_surface, (column*self.cell_size +50, row*self.cell_size +16, 50, 50))

                    cell_value = self.grid[row][column]
                    cell_rect = pygame.Rect(column*self.cell_size +30, row*self.cell_size +16,
                                            self.cell_size-27, self.cell_size-5)

                    # X and Y coord of its top left corner and its width and height
                    # The cell_rect line is also creating and drawing the gridlines if you look closely.
                    if row<20:
                        pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
                        screen.blit(dot, (column * self.cell_size + 37, row * self.cell_size + 28, 50, 50))
                    else:
                        screen.blit(ender, (column * self.cell_size + 25, row * self.cell_size + 20, 50, 50))
                else:
                    if column%2==0:
                        screen.blit(a, (column * self.cell_size + 25, row * self.cell_size + 28, 50, 50))
                    else:
                        screen.blit(b, (column * self.cell_size + 25, row * self.cell_size + 28, 50, 50))




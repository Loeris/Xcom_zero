import pygame
from Intro import intro


class Menu:
    def __init__(self):
        self.data = [[0] * width for _ in range(height)]
        self.left = 400
        self.top = 10
        self.size = 50

    def render(self, screen):
        x = self.left - 2 * self.size
        y = self.top - self.size
        for i in range(3):
            x += 2 * self.size
            for j in range(7):
                y += self.size
                pygame.draw.rect(screen,
                                 (0, 100, 255),  # цвет меню
                                 ((x, y), (2 * self.size, self.size)),
                                 1)  # толщина меню
            y = self.top - self.size


class Entity:
    def __init__(self):
        pass

    def move(self):
        pass

    def chance(self):
        pass


class Enemy(Entity):
    pass


class Soldier(Entity):
    pass


class Desk:
    def __init__(self):
        self.width = 7
        self.height = 7
        self.data = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.size = 50

    def on_click(self, cell_cords):
        cell = self.data[cell_cords[1]][cell_cords[0]]
        print(cell_cords[0], cell_cords[1])

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        return ((mouse_pos[0] - self.left) // self.size,
                (mouse_pos[1] - self.top) // self.size)

    def render(self, screen):  # вывод на экран
        x = self.left - self.size
        y = self.top - self.size
        for i in range(self.width):
            x += self.size
            for j in range(self.height):
                y += self.size
                pygame.draw.rect(screen,
                                 (0, 100, 255),  # цвет клетки
                                 ((x, y), (self.size, self.size)),
                                 1)  # толщина клетки
            y = self.top - self.size


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 500
    screen = pygame.display.set_mode(size)
    # intro(screen)
    desk = Desk()
    menu = Menu()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                desk.get_click(event.pos)
        screen.fill((255, 255, 255))  # цвет экрана
        desk.render(screen)
        menu.render(screen)
        pygame.display.flip()
    pygame.quit()

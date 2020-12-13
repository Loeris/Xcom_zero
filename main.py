import pygame
from Intro import intro

def sprite_rect(screen, cell):
    left = cell[1][0]
    top = cell[1][1]
    pygame.draw.rect(screen, (0, 0, 0),
                     ((left + border, top + border),
                      (border * 8, border * 3)),
                     border // 3)

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


class Menu:
    def __init__(self, w, h, le, t):
        self.wsize = border * 10
        self.hsize = border * 10
        self.width = w
        self.height = h
        self.left = le
        self.top = t
        self.color = (0, 100, 255)
        self.border = border // 3
        self.data = [[
            (0,
             (le + i * self.wsize, t + j * self.hsize)
             ) for i in range(self.width)] for j in range(self.height)]

    def render(self, screen):
        x = self.left - self.wsize
        y = self.top - self.hsize
        for i in range(self.width):
            x += self.wsize
            for j in range(self.height):
                y += self.hsize
                pygame.draw.rect(screen,
                                 self.color,
                                 ((x, y), (self.wsize, self.hsize)),
                                 self.border)
            y = self.top - self.hsize


class Table(Menu):
    def __init__(self, w, h, le, t):
        super(Table, self).__init__(w, h, le, t)
        self.wsize = 2 * self.hsize
        self.left = desk.left + desk.width * desk.wsize + border * 5


class Desk(Menu):
    def __init__(self, w, h, le, t):
        super(Desk, self).__init__(w, h, le, t)

    def on_click(self, cell_cords):
        print(cell_cords[1], cell_cords[0])
        for i in self.data:
            print(*i)
        cell = self.data[cell_cords[1]][cell_cords[0]]
        render_list.append((sprite_rect, cell))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.on_click(cell)

    def get_cell(self, mouse_pos):
        x = int((mouse_pos[0] - self.left) // self.wsize)
        y = int((mouse_pos[1] - self.top) // self.hsize)
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y


if __name__ == '__main__':
    pygame.init()
    render_list = []
    size = width, height = 1000, 500
    screen = pygame.display.set_mode(size)
    border = height // 80
    # intro(screen)
    desk = Desk(7, 7, border * 7, border * 2)
    table = Table(4, 6, border * 7, border * 2)
    table.top += table.hsize
    panel = Table(4, 1, border * 7, border * 2)
    panel.color = "red"
    panel.border *= 2
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                desk.get_click(event.pos)
        screen.fill((255, 255, 255))  # цвет экрана
        for func, cell in render_list:
            func(screen, cell)
        desk.render(screen)
        table.render(screen)
        panel.render(screen)
        pygame.display.flip()
    pygame.quit()

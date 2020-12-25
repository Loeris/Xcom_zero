from Intro import intro
from Sprites import *


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
             (le + i * self.wsize, t + j * self.hsize),
             (j, i)
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
        self.color = "red"

class Robot:
    def __init__(self, position, size):
        self.size = size
        self.position = position
        self.core = Rect((position[0]+2, position[1]+2), (size[0]-4, size[1]-4))
    
    def move(self, target):
        pass


class Desk(Menu):
    def __init__(self, w, h, le, t):
        super(Desk, self).__init__(w, h, le, t)
        self.current_cell = None

    def get_cell_by_point(self, pos):#возвращает ячейку массива по координатам клика
        pass

    def get_point_by_cell(self, cell):
        pass

    def on_click(self, cell_cords):
        cell = self.data[cell_cords[1]][cell_cords[0]]
        if self.current_cell is None and cell in (_[3] for _ in render_list):
            self.current_cell = cell
        elif self.current_cell is not None:
            sprite = render_list[[_[3] for _ in render_list].index(self.current_cell)][0]
            print(self.current_cell)
            print(cell)
            self.move(sprite, self.current_cell[2], cell[2])
            self.current_cell = None
        # render_list.append((sprite_support, cell[1][0], cell[1][1], cell))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.on_click(cell)

    def get_cell(self, mouse_pos):
        x = int((mouse_pos[0] - self.left) // self.wsize)
        y = int((mouse_pos[1] - self.top) // self.hsize)
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y

    def move(self, sprite, c1, c2):
        cell1 = self.data[c1[0]][c1[1]]
        cell2 = self.data[c2[0]][c2[1]]
        left1 = cell1[1][0]
        top1 = cell1[1][1]
        left2 = cell2[1][0]
        top2 = cell2[1][1]
        render_list.pop([_[3] for _ in render_list].index(self.current_cell))
        print('d')
        if top1 < top2:
            k = 1 * border // 3
        else:
            k = -1 * border // 3
        for i in range(top1, top2, k):
            screen.fill((255, 255, 255))  # цвет экрана
            for func, left, top, cell in render_list:
                func(screen, left, top)
            desk.render(screen)
            table.render(screen)
            sprite(screen, left1, i)
            pygame.time.wait(5)
            pygame.display.flip()
        if left1 < left2:
            k = 1 * border // 3
        else:
            k = -1 * border // 3
        for i in range(left1, left2, k):
            screen.fill((255, 255, 255))  # цвет экрана
            for func, left, top, cell in render_list:
                func(screen, left, top)
            desk.render(screen)
            table.render(screen)
            sprite(screen, i, top2)
            pygame.time.wait(5)
            pygame.display.flip()
        render_list.append((sprite, left2, top2, cell2))


class Robot_controller:
    def __init__(self, desk, robot_render, logic):
        self.desk = desk
        self.robot_render = robot_render
        self.logic = logic
        self.selected_robot = None
        self.path=[]
        self.point = None

    def click(self, click_pos):
        if len(self.path)>0:
            return
        cell = self.desk.get_cell_by_point(click_pos)
        if cell and self.selected_robot==None:
            self.select_robot(cell)
        elif cell and self.selected_robot and self.logic.canMove(cell, self.selected_robot):
            self.path = self.logic.move(self.selected_robot,cell)

    def select_robot(self, cell):
        self.selected_robot = self.logic.get_robot(coord)

    def update(self, screen):
        if self.selected_robot==None:
            return

        if len(path)==0 and self.point != None:
            self.selected_robot=None
        
        if self.desk.get_cell_by_point(self.point) == self.path[0]:
            self.point = None

        if self.point:
            self.robot_render.render_move_to(screen, self.point, self.selected_robot)
        elif len(path)>0 and self.point==None:
            self.point = get_point_by_cell(path.pop(0))
            



if __name__ == '__main__':
    pygame.init()
    render_list = []
    size = width,height = 1000, 500
    screen = pygame.display.set_mode(size)
    border = height // 80
    # intro(screen)
    desk = Desk(12, 8, border * 8, border * 2)
    table = Table(2, 2, border * 138, border * 2)
    running = True

    r_controller = Robot_controller(desk, None, None)

    # cell0 = desk.data[8][8]
    # render_list.append((sprite_alien, cell0[1][0], cell0[1][1], cell0))
    # cell0 = desk.data[1][7]
    # render_list.append((sprite_heavy, cell0[1][0], cell0[1][1], cell0))
    # cell0 = desk.data[1][4]
    # render_list.append((sprite_sniper, cell0[1][0], cell0[1][1], cell0))
    # cell0 = desk.data[3][8]
    # render_list.append((sprite_ranger, cell0[1][0], cell0[1][1], cell0))
    # cell0 = desk.data[3][3]
    # render_list.append((sprite_support, cell0[1][0], cell0[1][1], cell0))
    # cell0 = desk.data[8][8]
    # render_list.append((sprite_common, cell0[1][0], cell0[1][1], cell0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                r_controller.click(event.pos)
                #desk.get_click(event.pos)
        screen.fill((255, 255, 255))  # цвет экрана

        # for func, left, top, cell in render_list:
        #     func(screen, left, top)

        desk.render(screen)
        table.render(screen)
        r_controller.update(screen)

        pygame.display.flip()
    pygame.quit()
from Sprites import *
import pygame
from find import backward, fill_path

pygame.init()
preset0 = [
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', ],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', ],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', ],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', ],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', ],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', ],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', ],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', ]]
preset1 = [
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', ],
    ['e', 'e', 'e', 'e', 'b', 'e', 'e', 'e', 'e', 'e', 'e', 'e', ],
    ['e', 'b', 'B', 'B', 'b', 'e', 'e', 'e', 'e', 'e', 'e', 'e', ],
    ['e', 'B', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', ],
    ['e', 'b', 'B', 'B', 'B', 'b', 'e', 'e', 'e', 'e', 'e', 'e', ],
    ['e', 'e', 'e', 'e', 'e', 'B', 'e', 'b', 'B', 'b', 'e', 'e', ],
    ['e', 'e', 'e', 'e', 'e', 'b', 'B', 'b', 'e', 'e', 'e', 'e', ],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', ]]


class Bullet:
    def __init__(self, start, end, size):
        self.speed = 5
        self.start = start  # координаты откуда вылетает и куда летит пуля
        self.end = end
        self.left = start[0]  # значение х стартовой точки
        self.rect = pygame.Rect((start), (size, size))
        self.img = pygame.Surface((size, size))  # отрисовка пули
        self.top = start[1]  # значение у стартовой точки
        a = end[0] - start[0]  # для подсчета угла на который летит пуля
        b = end[1] - start[1]
        c = (a ** 2 + b ** 2) ** 0.5
        self.hit = False
        self.dx = a / c * self.speed  # скорость по х
        self.dy = b / c * self.speed  # скорость по y

    def move_bullet(self, list_target):
        self.rect.x = int(self.rect.x + self.dx)  # текущие координаты пули, dxскорость движения пули по оси
        self.rect.y = int(self.rect.y + self.dy)
        for item in list_target:
            target_rect = item.get_rect()
            if target_rect.colliderect(self.rect):  # colliderect = проверка пересечение двух прямоугольников
                return item
        return None

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    # движет пулю и проверяет столкнулась она с чем или нет
    def update(self, screen, list_target):  # запускает логику и графику пули
        result = self.move_bullet(list_target)
        self.draw(screen)
        return result


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
            [0,
             (le + i * self.wsize, t + j * self.hsize),
             (j, i)
             ] for i in range(self.width)] for j in range(self.height)]

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

    def get_cell(self, mouse_pos):
        x = int((mouse_pos[0] - self.left) // self.wsize)
        y = int((mouse_pos[1] - self.top) // self.hsize)
        if 0 <= x < self.width and 0 <= y < self.height:
            return x, y


class Buttons(Menu):
    def __init__(self, w, h, le, t):
        super(Buttons, self).__init__(w, h, le, t)
        self.color = "green"
        self.active = None

    def on_click(self, cell_cords):
        if cell_cords == (1, 2):
            con.start()
        elif cell_cords == (0, 0):
            self.active = "shot"


class Table(Menu):
    def __init__(self, w, h, le, t):
        super(Table, self).__init__(w, h, le, t)
        self.color = "red"
        self.sprite_circle = [sprite_heavy, sprite_sniper, sprite_support, sprite_ranger]
        self.sprite_list = [sprite_sniper, sprite_sniper, sprite_ranger, sprite_ranger]

    def on_click(self, cell_cords):
        num = [_[3] for _ in render_list].index(self.data[cell_cords[1]][cell_cords[0]])
        sprite = render_list[num][0]
        cell0 = render_list[num][3]
        render_list.pop(num)
        sprite = self.sprite_circle[(self.sprite_circle.index(sprite) + 1) % 4]
        render_list.append((sprite, cell0[1][0], cell0[1][1], cell0))
        if cell_cords == (0, 0):
            ind = 0
        elif cell_cords == (1, 0):
            ind = 1
        elif cell_cords == (0, 1):
            ind = 2
        elif cell_cords == (1, 1):
            ind = 3
        self.sprite_list[ind] = sprite


class Desk(Menu):
    def __init__(self, w, h, le, t, btn, controler):
        super(Desk, self).__init__(w, h, le, t)
        self.current_cell = None
        self.btn = btn
        self.target_shot = None
        self.controler = controler

    def kill_robots(self, item):  # уничтожение робота. item- в какого робота совершино поподание
        self.controler.kill_robots(item)
        self.remove(item)

    def remove(self, item):  # замена робота на пустую ячейку
        self.data[item.row][item.col] = ['e', (item.rect.x, item.rect.y), (item.row, item.col)]

    def on_click(self, cell_cords):
        cell = self.data[cell_cords[1]][cell_cords[0]]  # в какую ячейку кликнули
        if self.current_cell is None and cell[
            0] == "s":  # and cell in (_[3] for _ in render_list): # если робот не выбран и нажатая ячейка содержит робота выбрать его
            self.current_cell = cell
        elif self.current_cell is not None and cell[
            0] == "e":  # если робот выбран и кликнули в пустую ячейку перемещаем робота
            # sprite = render_list[[_[3] for _ in render_list].index(self.current_cell)][0]
            sprite = self.controler.robots_list[[_[3] for _ in self.controler.robots_list].index(self.current_cell)][0]
            self.data[self.current_cell[2][0]][self.current_cell[2][1]][0] = "e"
            self.move(sprite, self.find(self.current_cell[2], cell[2]))
            self.data[cell[2][0]][cell[2][1]][0] = "s"
            self.current_cell = None  # current_cell - выбранный робот
        elif self.current_cell and self.btn.active == "shot":  # если действие выстрелить
            self.target_shot = cell
            self.shot()
            self.target_shot = None
            self.current_cell = None
            self.btn.active = None

    def find(self, c1, c2):
        for j in range(len(self.data)):
            for i in range(len(self.data[j])):
                preset1[j][i] = self.data[j][i][0]
        preset = preset1
        x, y = c1
        c1 = (y, x)
        x, y = c2
        c2 = (y, x)
        fill_path(preset, c1, c2, 0)
        return backward(preset, c2, c1)

    def shot(self):  # создает пулю совершает выстрел
        bullet = Bullet(self.current_cell[1], self.target_shot[1], border * 5)
        self.controler.shot(bullet, self.current_cell)

    def move(self, sprite, path):  # движение робота
        # render_list.pop([_[3] for _ in render_list].index(self.current_cell))
        robot = self.controler.robots_list.pop([_[3] for _ in self.controler.robots_list].index(
            self.current_cell))  # сохраняю инфу о роботе, который пытаемся переместить
        for _1 in range(len(path) - 1):
            c1 = path[_1]
            c2 = path[_1 + 1]
            cell1 = self.data[c1[0]][c1[1]]
            cell2 = self.data[c2[0]][c2[1]]
            left1 = cell1[1][0]
            top1 = cell1[1][1]
            left2 = cell2[1][0]
            top2 = cell2[1][1]
            if top1 < top2:
                k = 1 * border // 3
            else:
                k = -1 * border // 3
            for _ in range(top1, top2, k):
                con.render()
                con.draw(sprite, left1, _)
                pygame.time.wait(5)
                pygame.display.flip()
            if left1 < left2:
                k = 1 * border // 3
            else:
                k = -1 * border // 3
            for _ in range(left1, left2, k):
                con.render()
                con.draw(sprite, _, top2)
                pygame.time.wait(5)
                pygame.display.flip()
        # render_list.append((sprite, left2, top2, cell2))
        self.controler.robots_list.append((sprite, left2, top2, cell2, robot[4]))


class Cell:  # инфа о ячейке
    def __init__(self, x, y, w, h, row, col, type_cell):
        self.rect = pygame.Rect((x, y), (w, h))
        self.type = type_cell
        self.row = row
        self.col = col

    def get_rect(self):  # прямоугольник клетки
        return self.rect

    def get_cell(self):  # координаты клетки
        return (self.row, self.col)

    def __str__(self):  # выводит на экран инфу о клетки строкой (нужен для отладки)
        return f"{self.rect}, {self.row}, {self.col}, {self.type}"


class Connector:
    def __init__(self):
        self.key1_list = []
        self.key2_list = []
        self.robots_list = []

    def kill_robots(self, item):
        self.robots_list = list(filter(lambda robot: robot[3][2] != item.get_cell(),
                                       self.robots_list))  # удаляем не нужного(убитого) робота из списка

    def init(self):  # инициализирует поля(поля = что именно где отрисовывать)
        self.key1_list = [table1.data[0][0], table1.data[0][1], table1.data[1][0], table1.data[1][1],
                          table2.data[0][0], table2.data[0][1], table2.data[1][0], table2.data[1][1],
                          buttons.data[0][0], buttons.data[1][0], buttons.data[2][0],
                          buttons.data[0][1], buttons.data[1][1], buttons.data[2][1]]

    def shot(self, bullet, owner):  # отрисовка выстрела
        print("shot")
        list_target = []
        for j in range(len(desk.data)):
            for i in range(len(desk.data[j])):
                cell = desk.data[j][i]
                if cell[0] in ("b", "B", "s") and cell != owner:
                    # pygame.Rect(cell[1], (border * 10, border * 10))
                    list_target.append(Cell(*cell[1], border * 10, border * 10, *cell[2], cell[0]))
        while True:
            self.render()
            target = bullet.update(screen, list_target)
            if target != None:
                if target.type == 's':
                    if self.check_team(target.get_cell(), owner[2]):
                        desk.kill_robots(target)
                break
            pygame.display.update()
            pygame.time.wait(5)

    def check_team(self, target, owner):
        target_team = list(filter(lambda robot: robot[3][2] == target, self.robots_list))[0][4]
        owner_team = list(filter(lambda robot: robot[3][2] == owner, self.robots_list))[0][4]
        if target_team == owner_team:
            return False
        return True

    def start(self):  # начальная расстановка спрайтов
        for j in range(len(desk.data)):
            for i in range(len(desk.data[j])):
                desk.data[j][i][0] = preset1[j][i]
        self.key2_list = [*table1.sprite_list, *table2.sprite_list,
                          sprite_shoot, sprite_move, sprite_map,
                          sprite_cancel, sprite_wait, sprite_restart]
        global render_list
        render_list = []
        sprite_list = [(desk.data[2][0], 1), (desk.data[3][0], 1), (desk.data[4][0], 1), (desk.data[5][0], 1),
                       (desk.data[2][-1], 2), (desk.data[3][-1], 2), (desk.data[4][-1], 2), (desk.data[5][-1], 2)]

        for _ in range(len(self.key2_list)):
            cell0 = self.key1_list[_]
            render_list.append((self.key2_list[_], cell0[1][0], cell0[1][1], cell0))

        for _ in range(8):
            cell0, team = sprite_list[_]
            self.robots_list.append((self.key2_list[_], cell0[1][0], cell0[1][1], cell0, team))
            # render_list.append((self.key2_list[_], cell0[1][0], cell0[1][1], cell0))
            desk.data[cell0[2][0]][cell0[2][1]][0] = "s"

    def draw(self, sprite, left, top):
        sprite(screen, left, top)

    def get_click(self, mouse_pos):
        cell = desk.get_cell(mouse_pos)
        if cell is not None:
            desk.on_click(cell)
        else:
            cell = table1.get_cell(mouse_pos)
            if cell is not None:
                table1.on_click(cell)
            else:
                cell = table2.get_cell(mouse_pos)
                if cell is not None:
                    table2.on_click(cell)
                else:
                    cell = buttons.get_cell(mouse_pos)
                    if cell is not None:
                        buttons.on_click(cell)

    def render(self):
        screen.fill((255, 255, 255))  # цвет экрана
        for sprite, left, top, cell in render_list:
            self.draw(sprite, left, top)
        for sprite, left, top, cell, team in self.robots_list:
            self.draw(sprite, left, top)
        desk.render(screen)  # рисуем доску
        table1.render(screen)  # рисуем окно выбора солдат 1 игрока
        table2.render(screen)  # рисуем окно выбора солдат 2 игрока
        buttons.render(screen)  # рисуем кнопки действия
        for j in range(desk.height):  # рисуем препятствия
            for i in range(desk.width):
                if desk.data[j][i][0] == "b":
                    left, top = desk.data[j][i][1]
                    self.draw(sprite_swall, left, top)
                if desk.data[j][i][0] == "B":
                    left, top = desk.data[j][i][1]
                    self.draw(sprite_bwall, left, top)


if __name__ == '__main__':
    render_list = []
    size = width, height = 1000, 500
    screen = pygame.display.set_mode(size)
    border = height // 80
    # intro(screen)
    con = Connector()
    buttons = Buttons(2, 3, border * 138, border * 44)
    desk = Desk(12, 8, border * 8, border * 2, buttons, con)
    table1 = Table(2, 2, border * 138, border * 2)
    table2 = Table(2, 2, border * 138, border * 23)
    con.init()

    running = True
    con.start()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                con.get_click(event.pos)
        con.render()
        pygame.display.flip()
    pygame.quit()
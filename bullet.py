import pygame

# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 650  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#000000"

pygame.init()  # Инициация PyGame, обязательная строчка

clock = pygame.time.Clock()

screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко


class Bullet:
    def __init__(self, start, end, speed):
        self.start = start
        self.end = end
        self.rect = img.get_rect()  # присваиваем картинке прямоугольник
        self.rect.x = start[0]
        self.rect.y = start[1]
        a = end[0] - start[0]  # для подсчета угла на который летит пуля
        b = end[1] - start[1]
        c = ((a) ** 2 + (b) ** 2) ** 0.5
        self.hit = False
        self.dx = a / c * speed  # скорость по х
        self.dy = b / c * speed

    def move_bullet(self, list_target):
        self.rect.x = int(self.rect.x + self.dx)  # текущие координаты пули
        self.rect.y = int(self.rect.y + self.dy)
        for item in list_target:
            if item.colliderect(self.rect):  # colliderect = проверка пересечение двух прямоугольников
                self.hit = True

    def draw(self, screen):
        screen.blit(img, self.rect)

    def isHit(self):
        return self.hit


b1 = Bullet((0, 0), (50, 100), 5)
rect = pygame.Rect(50, 100, 10, 10)

list_target = [rect]

while 1:
    for e in pygame.event.get():  # Обрабатываем события
        if e.type == pygame.QUIT:
            raise SystemExit

    screen.fill(pygame.Color(BACKGROUND_COLOR))
    if b1.isHit() == False:  # пока пуля не сталкнулась, она летит
        b1.move_bullet(list_target)
        b1.draw(screen)
    pygame.display.update()
    clock.tick(120)

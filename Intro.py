import pygame
import random
def intro(screen):
    s = [(random.random() * 800, random.random() * 400, 1, 1) for i in range(2000)]
    if True:
        color = pygame.Color(255, 255, 100)
        for i in s:
            screen.fill(pygame.Color('white'),
                        i)
            pygame.draw.circle(screen, (0, 0, 0), (400, 200), 45)
            pygame.display.flip()
        for i in range(11):
            pygame.draw.circle(screen, color, (400, 200), i)
            pygame.display.flip()
            pygame.time.wait(10)
        for i in range(41):
            pygame.draw.circle(screen, color, (400, 200), 10 + i)
            pygame.draw.circle(screen, (0, 0, 0), (400, 200), 5 + i)
            pygame.draw.circle(screen, color, (400, 200), 10)
            pygame.display.flip()
            pygame.time.wait(10)
        for i in range(25, 200):
            pygame.draw.line(screen, color, (400 - 2 * i, 200 - i),
                             (400 + 2 * i, 200 + i), 5)
            pygame.draw.line(screen, color, (400 - 2 * i, 200 + i),
                             (400 + 2 * i, 200 - i), 5)
            pygame.draw.line(screen, color, (400, 200 - i),
                             (400, 200 + i), 5)
            pygame.draw.line(screen, color, (400 - 2 * i, 200),
                             (400 + 2 * i, 200), 5)
            pygame.draw.circle(screen, color, (400, 200), 50)  # O
            pygame.draw.circle(screen, (0, 0, 0), (400, 200), 45)  # O
            pygame.draw.circle(screen, color, (400, 200), 10)  # O
            pygame.display.flip()
            pygame.time.wait(1)
        for i in range(200):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(400 - 2 * i, 200 - i,
                                                            4 * i, 2 * i))  # Прорезь
            for i in s:
                screen.fill(pygame.Color('white'),
                            i)
            pygame.draw.circle(screen, color, (400, 200), 50)  # O
            pygame.draw.circle(screen, (0, 0, 0), (400, 200), 45)  # O
            pygame.draw.circle(screen, color, (400, 200), 10)  # O
            pygame.display.flip()
        hsv = color.hsva
        for i in range(100):
            color.hsva = (hsv[0], hsv[1], i, hsv[3])
            pygame.draw.line(screen, color, (230, 150), (200, 250), 5)  # A
            pygame.draw.line(screen, color, (250, 210), (210, 210), 5)  # A
            pygame.draw.line(screen, color, (230, 150), (260, 250), 5)  # A
            pygame.draw.line(screen, color, (280, 250), (280, 150), 5)  # L
            pygame.draw.line(screen, color, (280, 248), (340, 248), 5)  # L
            pygame.draw.line(screen, color, (470, 250), (470, 150), 5)  # N
            pygame.draw.line(screen, color, (530, 250), (470, 150), 5)  # N
            pygame.draw.line(screen, color, (530, 250), (530, 150), 5)  # N
            pygame.draw.line(screen, color, (550, 250), (550, 150), 5)  # E
            pygame.draw.line(screen, color, (550, 248), (600, 248), 5)  # E
            pygame.draw.line(screen, color, (550, 200), (600, 200), 5)  # E
            pygame.draw.line(screen, color, (550, 152), (600, 152), 5)  # E
            pygame.display.flip()
            pygame.time.wait(10)
        pygame.time.wait(50)
        for i in range(100):
            color.hsva = (hsv[0], hsv[1], 100 - i, hsv[3])
            pygame.draw.line(screen, color, (230, 150), (200, 250), 5)  # A
            pygame.draw.line(screen, color, (250, 210), (210, 210), 5)  # A
            pygame.draw.line(screen, color, (230, 150), (260, 250), 5)  # A
            pygame.draw.line(screen, color, (280, 250), (280, 150), 5)  # L
            pygame.draw.line(screen, color, (280, 248), (340, 248), 5)  # L
            pygame.draw.circle(screen, color, (400, 200), 50)  # O
            pygame.draw.circle(screen, (0, 0, 0), (400, 200), 45)  # O
            pygame.draw.circle(screen, color, (400, 200), 10)  # O
            pygame.draw.line(screen, color, (470, 250), (470, 150), 5)  # N
            pygame.draw.line(screen, color, (530, 250), (470, 150), 5)  # N
            pygame.draw.line(screen, color, (530, 250), (530, 150), 5)  # N
            pygame.draw.line(screen, color, (550, 250), (550, 150), 5)  # E
            pygame.draw.line(screen, color, (550, 248), (600, 248), 5)  # E
            pygame.draw.line(screen, color, (550, 200), (600, 200), 5)  # E
            pygame.draw.line(screen, color, (550, 152), (600, 152), 5)  # E
            pygame.display.flip()
            pygame.time.wait(15)
        for i in s:
            screen.fill(pygame.Color('black'),
                        i)
            pygame.display.flip()
        for i in range(255):
            screen.fill((i, i, i))
            pygame.display.flip()
            pygame.time.wait(7)

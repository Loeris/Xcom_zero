import pygame
import random


def intro(screen):
    width = screen.get_width()
    height = screen.get_height()
    border = height // 80
    stars = 5 * width // 2
    s = [(random.random() * width, random.random() * height, 1, 1) for _ in range(stars)]
    if True:
        color = pygame.Color(255, 255, 100)
        for i in s:
            screen.fill(pygame.Color('white'),
                        i)
            pygame.draw.circle(screen, (0, 0, 0), (width // 2, height // 2), border * 9)
            pygame.display.flip()
        for i in range(border * 2 + 1):
            pygame.draw.circle(screen, color, (width // 2, height // 2), i)
            pygame.display.flip()
            pygame.time.wait(10)
        for i in range(border * 8 + 1):
            pygame.draw.circle(screen, color, (width // 2, height // 2), border * 2 + i)
            pygame.draw.circle(screen, (0, 0, 0), (width // 2, height // 2), border + i)
            pygame.draw.circle(screen, color, (width // 2, height // 2), border * 2)
            pygame.display.flip()
            pygame.time.wait(10)
        for i in range(border * 2, height // 2):
            pygame.draw.line(screen, color, (width // 2 - 2 * i, height // 2 - i),
                             (width // 2 + 2 * i, height // 2 + i), border)
            pygame.draw.line(screen, color, (width // 2 - 2 * i, height // 2 + i),
                             (width // 2 + 2 * i, height // 2 - i), border)
            pygame.draw.line(screen, color, (width // 2, height // 2 - i),
                             (width // 2, height // 2 + i), border)
            pygame.draw.line(screen, color, (width // 2 - 2 * i, height // 2),
                             (width // 2 + 2 * i, height // 2), border)
            pygame.draw.circle(screen, color, (width // 2, height // 2), border * 10)  # O
            pygame.draw.circle(screen, (0, 0, 0), (width // 2, height // 2), border * 9)  # O
            pygame.draw.circle(screen, color, (width // 2, height // 2), border * 2)  # O
            pygame.display.flip()
            pygame.time.wait(1)
        for i in range(height // 2):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(width // 2 - 2 * i, height // 2 - i,
                                                            4 * i, 2 * i))  # Прорезь
            for j in s:
                screen.fill(pygame.Color('white'),
                            j)
            pygame.draw.circle(screen, color, (width // 2, height // 2), border * 10)  # O
            pygame.draw.circle(screen, (0, 0, 0), (width // 2, height // 2), border * 9)  # O
            pygame.draw.circle(screen, color, (width // 2, height // 2), border * 2)  # O
            pygame.display.flip()
        hsv = color.hsva
        for i in range(100):
            color.hsva = (hsv[0], hsv[1], i, hsv[3])
            pygame.draw.line(screen, color, (width // 2 - border * 34, height // 2 - border * 10),
                             (width // 2 - border * 40, height // 2 + border * 10), border)  # A
            pygame.draw.line(screen, color, (width // 2 - border * 30, height // 2 + border * 2),
                             (width // 2 - border * 38, height // 2 + border * 2), border)  # A
            pygame.draw.line(screen, color, (width // 2 - border * 34, height // 2 - border * 10),
                             (width // 2 - border * 28, height // 2 + border * 10), border)  # A
            pygame.draw.line(screen, color, (width // 2 - border * 24, height // 2 + border * 10),
                             (width // 2 - border * 24, height // 2 - border * 10), border)  # L
            pygame.draw.line(screen, color, (width // 2 - border * 24, height // 2 + border * 10 - border // 2),
                             (width // 2 - border * 12, height // 2 + border * 10 - border // 2), border)  # L
            pygame.draw.line(screen, color, (width // 2 + border * 14, height // 2 + border * 10),
                             (width // 2 + border * 14, height // 2 - border * 10), border)  # N
            pygame.draw.line(screen, color, (width // 2 + border * 26, height // 2 + border * 10),
                             (width // 2 + border * 14, height // 2 - border * 10), border)  # N
            pygame.draw.line(screen, color, (width // 2 + border * 26, height // 2 + border * 10),
                             (width // 2 + border * 26, height // 2 - border * 10), border)  # N
            pygame.draw.line(screen, color, (width // 2 + border * 30, height // 2 + border * 10),
                             (width // 2 + border * 30, height // 2 - border * 10), border)  # E
            pygame.draw.line(screen, color, (width // 2 + border * 30, height // 2 + border * 10 - border // 2),
                             (width // 2 + border * 40, height // 2 + border * 10 - border // 2), border)  # E
            pygame.draw.line(screen, color, (width // 2 + border * 30, height // 2),
                             (width // 2 + border * 40, height // 2), border)  # E
            pygame.draw.line(screen, color, (width // 2 + border * 30, height // 2 - border * 10 + border // 2),
                             (width // 2 + border * 40, height // 2 - border * 10 + border // 2), border)  # E
            pygame.display.flip()
            pygame.time.wait(10)
        pygame.time.wait(50)
        for i in range(100):
            color.hsva = (hsv[0], hsv[1], 100 - i, hsv[3])
            pygame.draw.line(screen, color, (width // 2 - border * 34, height // 2 - border * 10),
                             (width // 2 - border * 40, height // 2 + border * 10), border)  # A
            pygame.draw.line(screen, color, (width // 2 - border * 30, height // 2 + border * 2),
                             (width // 2 - border * 38, height // 2 + border * 2), border)  # A
            pygame.draw.line(screen, color, (width // 2 - border * 34, height // 2 - border * 10),
                             (width // 2 - border * 28, height // 2 + border * 10), border)  # A
            pygame.draw.line(screen, color, (width // 2 - border * 24, height // 2 + border * 10),
                             (width // 2 - border * 24, height // 2 - border * 10), border)  # L
            pygame.draw.line(screen, color, (width // 2 - border * 24, height // 2 + border * 10 - border // 2),
                             (width // 2 - border * 12, height // 2 + border * 10 - border // 2), border)  # L
            pygame.draw.circle(screen, color, (width // 2, height // 2), border * 10)  # O
            pygame.draw.circle(screen, (0, 0, 0), (width // 2, height // 2), border * 9)  # O
            pygame.draw.circle(screen, color, (width // 2, height // 2), border * 2)  # O
            pygame.draw.line(screen, color, (width // 2 + border * 14, height // 2 + border * 10),
                             (width // 2 + border * 14, height // 2 - border * 10), border)  # N
            pygame.draw.line(screen, color, (width // 2 + border * 26, height // 2 + border * 10),
                             (width // 2 + border * 14, height // 2 - border * 10), border)  # N
            pygame.draw.line(screen, color, (width // 2 + border * 26, height // 2 + border * 10),
                             (width // 2 + border * 26, height // 2 - border * 10), border)  # N
            pygame.draw.line(screen, color, (width // 2 + border * 30, height // 2 + border * 10),
                             (width // 2 + border * 30, height // 2 - border * 10), border)  # E
            pygame.draw.line(screen, color, (width // 2 + border * 30, height // 2 + border * 10 - border // 2),
                             (width // 2 + border * 40, height // 2 + border * 10 - border // 2), border)  # E
            pygame.draw.line(screen, color, (width // 2 + border * 30, height // 2),
                             (width // 2 + border * 40, height // 2), border)  # E
            pygame.draw.line(screen, color, (width // 2 + border * 30, height // 2 - border * 10 + border // 2),
                             (width // 2 + border * 40, height // 2 - border * 10 + border // 2), border)  # E
            pygame.display.flip()
            pygame.time.wait(15)
        """for i in s:
            screen.fill(pygame.Color('black'),
                        i)
            pygame.display.flip()"""
        """for i in range(255):
            screen.fill((i, i, i))
            pygame.display.flip()
            pygame.time.wait(7)"""

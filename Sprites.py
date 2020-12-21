import pygame
pygame.init()
def sprite_template(screen, left, top):
    border = screen.get_height() // 80
    s = [
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != None:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))


def sprite_alien(screen, left, top):
    border = screen.get_height() // 80
    c = "purple"
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, c, c, c, c, 0, 0, 0],
        [0, 0, c, 0, c, c, 0, c, 0, 0],
        [0, 0, c, c, c, c, c, c, 0, 0],
        [0, 0, 0, c, 0, 0, c, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))


def sprite_heavy(screen, left, top):
    border = screen.get_height() // 80
    z = (0, 0, 0)
    c = (213, 0, 0)
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, c, 0, z, z, 0, c, 0, 0],
        [0, z, c, c, z, z, c, c, z, 0],
        [0, z, c, c, c, c, c, c, z, 0],
        [0, z, 0, 0, c, c, 0, 0, z, 0],
        [0, z, 0, z, c, c, z, 0, z, 0],
        [0, 0, 0, z, 0, 0, z, 0, 0, 0],
        [0, 0, 0, z, 0, 0, z, 0, 0, 0],
        [0, 0, 0, z, 0, 0, z, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))


def sprite_sniper(screen, left, top):
    border = screen.get_height() // 80
    z = (0, 0, 0)
    c = (3, 169, 244)
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, c, 0, 0, z, z, 0, 0, c, 0],
        [0, c, 0, 0, z, z, 0, 0, c, 0],
        [0, 0, c, c, c, c, c, c, 0, 0],
        [0, 0, z, 0, c, c, 0, z, 0, 0],
        [0, 0, z, c, z, z, c, z, 0, 0],
        [0, c, c, 0, z, z, 0, c, c, 0],
        [0, 0, 0, z, 0, 0, z, 0, 0, 0],
        [0, 0, 0, z, 0, 0, z, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))


def sprite_ranger(screen, left, top):
    border = screen.get_height() // 80
    z = (0, 0, 0)
    c = (255, 152, 0)
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, z, z, 0, 0, 0, 0],
        [0, c, 0, 0, z, z, 0, 0, c, 0],
        [0, 0, c, c, z, z, c, c, 0, 0],
        [0, 0, z, c, z, z, c, z, 0, 0],
        [0, 0, z, 0, z, z, 0, z, 0, 0],
        [0, 0, 0, 0, z, z, 0, 0, 0, 0],
        [0, 0, 0, z, 0, 0, z, 0, 0, 0],
        [0, 0, 0, c, 0, 0, c, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))


def sprite_support(screen, left, top):
    border = screen.get_height() // 80
    z = (0, 0, 0)
    c = (76, 175, 80)
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, c, 0, z, z, 0, c, 0, 0],
        [0, 0, c, 0, z, z, 0, c, 0, 0],
        [0, c, c, c, c, c, c, c, c, 0],
        [0, 0, z, 0, z, z, 0, z, 0, 0],
        [0, 0, z, 0, z, z, 0, z, 0, 0],
        [0, 0, 0, 0, z, z, 0, 0, 0, 0],
        [0, c, 0, z, 0, 0, z, 0, c, 0],
        [0, c, c, z, 0, 0, z, c, c, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))


def sprite_common(screen, left, top):
    border = screen.get_height() // 80
    z = (0, 0, 0)
    c = (158, 158, 158)
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, z, z, 0, 0, 0, 0],
        [0, 0, 0, 0, z, z, 0, 0, 0, 0],
        [0, 0, 0, z, c, c, z, 0, 0, 0],
        [0, 0, z, 0, c, c, 0, z, 0, 0],
        [0, 0, z, 0, c, c, 0, z, 0, 0],
        [0, 0, 0, 0, z, z, 0, 0, 0, 0],
        [0, 0, 0, z, 0, 0, z, 0, 0, 0],
        [0, 0, 0, z, 0, 0, z, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))
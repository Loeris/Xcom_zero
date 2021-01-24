import pygame

pygame.init()


def sprite_template(screen, left, top):
    border = screen.get_height() // 80
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))


def sprite_bwall(screen, left, top):
    border = screen.get_height() // 80
    c = (190, 190, 190)
    b = (210, 210, 210)
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, c, c, c, c, c, c, c, c, 0],
        [0, c, c, c, c, c, c, c, c, 0],
        [0, c, c, b, b, b, b, c, c, 0],
        [0, c, c, b, b, b, b, c, c, 0],
        [0, c, c, b, b, b, b, c, c, 0],
        [0, c, c, b, b, b, b, c, c, 0],
        [0, c, c, c, c, c, c, c, c, 0],
        [0, c, c, c, c, c, c, c, c, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))

def sprite_swall(screen, left, top):
    border = screen.get_height() // 80
    c = (190, 190, 190)
    b = (210, 210, 210)
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, c, c, c, c, 0, 0, 0],
        [0, 0, c, c, b, b, c, c, 0, 0],
        [0, c, c, b, b, b, b, c, c, 0],
        [0, c, c, b, b, b, b, c, c, 0],
        [0, c, c, b, b, b, b, c, c, 0],
        [0, c, c, c, c, c, c, c, c, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))


def sprite_shoot(screen, left, top):
    border = screen.get_height() // 80
    c = "green"
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, c, c, 0, 0, 0, 0],
        [0, 0, 0, 0, c, c, 0, 0, 0, 0],
        [0, 0, 0, c, 0, 0, c, 0, 0, 0],
        [0, c, c, 0, c, c, 0, c, c, 0],
        [0, c, c, 0, c, c, 0, c, c, 0],
        [0, 0, 0, c, 0, 0, c, 0, 0, 0],
        [0, 0, 0, 0, c, c, 0, 0, 0, 0],
        [0, 0, 0, 0, c, c, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))

def sprite_move(screen, left, top):
    border = screen.get_height() // 80
    c = "green"
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, c, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, c, c, 0, 0],
        [0, c, c, c, c, c, c, c, c, 0],
        [0, c, c, c, c, c, c, c, c, 0],
        [0, 0, 0, 0, 0, 0, c, c, 0, 0],
        [0, 0, 0, 0, 0, 0, c, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))

def sprite_cancel(screen, left, top):
    border = screen.get_height() // 80
    c = "green"
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, c, c, 0, 0, 0, 0, c, c, 0],
        [0, c, c, c, 0, 0, c, c, c, 0],
        [0, 0, c, c, c, c, c, c, 0, 0],
        [0, 0, 0, c, c, c, c, 0, 0, 0],
        [0, 0, 0, c, c, c, c, 0, 0, 0],
        [0, 0, c, c, c, c, c, c, 0, 0],
        [0, c, c, c, 0, 0, c, c, c, 0],
        [0, c, c, 0, 0, 0, 0, c, c, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))

def sprite_wait(screen, left, top):
    border = screen.get_height() // 80
    c = "green"
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, c, c, 0, c, c, 0, c, c, 0],
        [0, c, c, 0, c, c, 0, c, c, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))

def sprite_map(screen, left, top):
    border = screen.get_height() // 80
    c = "green"
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, c, c, c, c, c, c, c, c, 0],
        [0, c, 0, 0, 0, 0, 0, 0, c, 0],
        [0, c, 0, 0, 0, 0, 0, 0, c, 0],
        [0, c, 0, c, 0, c, 0, 0, c, 0],
        [0, c, 0, 0, c, 0, 0, 0, c, 0],
        [0, c, 0, c, 0, c, 0, 0, c, 0],
        [0, c, 0, 0, 0, 0, 0, 0, c, 0],
        [0, c, c, c, c, c, c, c, c, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))

def sprite_restart(screen, left, top):
    border = screen.get_height() // 80
    c = "green"
    s = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, c, c, c, 0, 0, 0, 0],
        [0, 0, c, c, c, c, c, 0, c, 0],
        [0, 0, 0, 0, 0, c, c, c, c, 0],
        [0, c, c, c, c, 0, c, c, c, 0],
        [0, c, c, c, 0, c, c, c, c, 0],
        [0, c, c, c, c, 0, 0, 0, 0, 0],
        [0, c, 0, c, c, c, c, c, 0, 0],
        [0, 0, 0, 0, c, c, c, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for j in range(len(s)):
        for i in range(len(s[j])):
            if s[j][i] != 0:
                pygame.draw.rect(screen, s[j][i],
                                 ((left + border * i, top + border * j),
                                  (border, border)))

def sprite_bullet(screen, left, top):
    border = screen.get_height() // 80
    c = "yellow"
    pygame.draw.circle(screen, c,
                       (left + border * 5, top + border * 5), border * 2)


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
        [0, c, c, z, 0, 0, z, c, c, 0],
        [0, c, c, z, 0, 0, z, c, c, 0],
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
        [0, c, 0, z, 0, 0, z, 0, c, 0],
        [0, c, 0, z, 0, 0, z, 0, c, 0],
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
        [0, c, 0, 0, z, z, 0, 0, c, 0],
        [0, c, 0, z, 0, 0, z, 0, c, 0],
        [0, c, 0, c, 0, 0, c, 0, c, 0],
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

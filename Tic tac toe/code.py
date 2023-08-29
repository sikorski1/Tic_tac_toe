import pygame
from sys import exit
from random import choice
from random import randint
from time import sleep


class Board:
    def __init__(self):
        self.line = pygame.Surface((10, 320))
        self.line_rotated = pygame.transform.rotate(self.line, 90)
        self.square = pygame.Surface((100, 100))
        self.squeres_rect = []

    def draw_board(self):
        line_rect1 = self.line.get_rect(midleft=(140, 200))
        line_rect2 = self.line.get_rect(midleft=(250, 200))
        line_rect3 = self.line_rotated.get_rect(midtop=(200, 140))
        line_rect4 = self.line_rotated.get_rect(midtop=(200, 250))
        screen.blit(self.line, line_rect1)
        screen.blit(self.line, line_rect2)
        screen.blit(self.line_rotated, line_rect3)
        screen.blit(self.line_rotated, line_rect4)
        for i in range(0, 9):
            if i < 3:
                self.square.fill((100, 100, 105))
                self.squeres_rect.append(self.square.get_rect(topleft=(40 + i * 110, 40)))
                screen.blit(self.square, self.squeres_rect[i])
            elif i < 6:
                self.square.fill((100, 100, 105))
                self.squeres_rect.append(self.square.get_rect(topleft=(40 + (i - 3) * 110, 150)))
                screen.blit(self.square, self.squeres_rect[i])
            else:
                self.square.fill((100, 100, 105))
                self.squeres_rect.append(self.square.get_rect(topleft=(40 + (i - 6) * 110, 260)))
                screen.blit(self.square, self.squeres_rect[i])


class Object:
    def __init__(self):
        self.circle = pygame.image.load("graphics/circle.png").convert_alpha()
        self.cross = pygame.image.load("graphics/cross.png").convert_alpha()

    def draw_object(self, rect, num):
        if num % 2 == 0:
            screen.blit(self.circle, rect)
        else:
            screen.blit(self.cross, rect)

    def return_obj(self, num):
        if num % 2 == 0:
            return "circle"
        else:
            return "cross"


class Game:
    def __init__(self):
        self.object = Object()
        self.board = Board()
        self.score_cross = pygame.image.load("graphics/score_cross.png").convert_alpha()
        self.score_circle = pygame.image.load("graphics/score_circle.png").convert_alpha()
        self.game_font = pygame.font.Font("font/Pixeltype.ttf", 50)
        self.score_font = pygame.font.Font("font/Pixeltype.ttf", 37)
        self.circle_pts = 0
        self.cross_pts = 0
        self.field_container = {}
        self.game_active = True

    def checking_status(self):
        for i in range(0, 9, 3):
            if (self.field_container.get(i) == "cross" and self.field_container.get(
                    i + 1) == "cross" and self.field_container.get(i + 2) == "cross") or \
                    (self.field_container.get(i) == "circle" and self.field_container.get(
                        i + 1) == "circle" and self.field_container.get(i + 2) == "circle"):
                return 1
        for i in range(0, 3):
            if (self.field_container.get(i) == "cross" and self.field_container.get(
                    i + 3) == "cross" and self.field_container.get(i + 6) == "cross") or \
                    (self.field_container.get(i) == "circle" and self.field_container.get(
                        i + 3) == "circle" and self.field_container.get(i + 6) == "circle"):
                return 1
        if (self.field_container.get(0) == "cross" and self.field_container.get(
                4) == "cross" and self.field_container.get(8) == "cross") or \
                (self.field_container.get(0) == "circle" and self.field_container.get(
                    4) == "circle" and self.field_container.get(8) == "circle"):
            return 1
        if (self.field_container.get(2) == "cross" and self.field_container.get(
                4) == "cross" and self.field_container.get(6) == "cross") or \
                (self.field_container.get(2) == "circle" and self.field_container.get(
                    4) == "circle" and self.field_container.get(6) == "circle"):
            return 1
        if len(self.field_container) == 9:
            return 2

    def display_result(self, obj):
        result_surf = self.game_font.render(obj.upper() + " WINS", False, "Black")
        space_surf = self.game_font.render("PRESS SPACE TO CONTINUE", False, "Black")
        result_rect = result_surf.get_rect(center=(200, 20))
        space_rect = space_surf.get_rect(center=(200, 380))
        screen.blit(result_surf, result_rect)
        screen.blit(space_surf, space_rect)

    def display_draw(self):
        result_surf = self.game_font.render("DRAW", False, "Black")
        space_surf = self.game_font.render("PRESS SPACE TO CONTINUE", False, "Black")
        result_rect = result_surf.get_rect(center=(200, 20))
        space_rect = space_surf.get_rect(center=(200, 380))
        screen.blit(result_surf, result_rect)
        screen.blit(space_surf, space_rect)

    def display_points(self):
        circle_rect = self.score_circle.get_rect(topleft=(10, 10))
        score_circle_surf = self.score_font.render(str(self.circle_pts), False, (0, 0, 0))
        score_circle_rect = score_circle_surf.get_rect(midtop=(26, 42))
        cross_rect = self.score_cross.get_rect(topright=(390, 10))
        score_cross_surf = self.score_font.render(str(self.cross_pts), False, (0, 0, 0))
        score_cross_rect = score_circle_surf.get_rect(midtop=(374, 42))
        screen.blit(self.score_circle, circle_rect)
        screen.blit(score_circle_surf, score_circle_rect)
        screen.blit(self.score_cross, cross_rect)
        screen.blit(score_cross_surf, score_cross_rect)

    def new_game(self):
        self.field_container.clear()
        self.board.squeres_rect.clear()
        screen.fill((100, 100, 105))
        self.board.draw_board()
        self.game_active = True


pygame.init()
SCREEN_WIDTH = 400
SCREEN_HIGH = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGH))
cell_size = 100
clock = pygame.time.Clock()
pygame.display.set_caption("Cross and Circle")
screen.fill((100, 100, 105))
num = randint(0, 1)

game = Game()
game.board.draw_board()
game_active = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        for i, rect in enumerate(game.board.squeres_rect):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos) and game.game_active:
                    if not i in game.field_container:
                        game.object.draw_object(rect, num)
                        obj = game.object.return_obj(num)
                        game.field_container[i] = obj
                        num += 1
                    else:
                        print("Not available")
    obj = game.object.return_obj(num - 1)
    keys = pygame.key.get_pressed()
    game.display_points()
    if game.checking_status() == 1:
        game.display_result(obj)
        game.game_active = False
        if keys[pygame.K_SPACE]:
            if obj == "circle":
                game.circle_pts += 1
            if obj == "cross":
                game.cross_pts += 1
            game.new_game()
    if game.checking_status() == 2:
        game.display_draw()
        game.game_active = False
        if keys[pygame.K_SPACE]:
            game.new_game()
    pygame.display.update()
    clock.tick(60)

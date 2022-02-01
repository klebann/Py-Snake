from turtle import position
import pygame
import time
import settings
from pygame.locals import *
from .snake.snake import Snake
from .food import Food


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Py-Snake")

        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode((1000, 800))
        self.surface.fill((0, 100, 0))
        self.snake = Snake(self.surface, 2)
        self.food = Food(self.surface)

        self.move_time = 0.3

        self.snake.draw()
        self.food.draw()

    def run(self):
        running = True
        self.pause = False
        lastFrameTime = time.time()

        while running:
            dt = time.time() - lastFrameTime

            running = self.events()

            if dt > self.move_time:
                lastFrameTime = time.time()
                try:
                    if not self.pause:
                        self.play()
                except NameError:
                    self.show_game_over()
                    self.pause = True

    def play(self):
        self.snake.walk()

        self.draw()

        # Snake collision with food
        if self.is_collision(self.snake.get_head_position(), self.food.get_position()):
            self.play_sound("ding")
            self.food.set_position()
            self.snake.grow()

        # Snake collision with itself
        for i in range(0, self.snake.length - 1):
            if self.is_collision(self.snake.get_head_position(), self.snake.get_body_position(i)):
                self.play_sound("crash")
                raise NameError("GameOver")

    def draw(self):
        self.render_background()

        self.food.draw()
        self.snake.draw()
        self.display_score()

        pygame.display.flip()

    def events(self):

        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
                if event.key == K_RETURN:
                    self.reset()
                if event.key == K_UP:
                    self.snake.move_up()
                if event.key == K_DOWN:
                    self.snake.move_down()
                if event.key == K_RIGHT:
                    self.snake.move_right()
                if event.key == K_LEFT:
                    self.snake.move_left()

        return True

    def is_collision(self, position1, position2):
        x1, y1 = position1
        x2, y2 = position2
        if x1 >= x2 and x1 < x2 + settings.SIZE:
            if y1 >= y2 and y1 < y2 + settings.SIZE:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(
            f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (800, 10))

    def show_game_over(self):
        self.surface.fill(settings.BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(
            f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        line2 = font.render(
            "To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 350))

        pygame.display.flip()

        pygame.mixer.music.pause()

    def reset(self):
        self.pause = False
        self.snake = Snake(self.surface, 2)
        self.food = Food(self.surface)
        pygame.mixer.music.unpause()

    def play_sound(self, name):
        sound = pygame.mixer.Sound(f"resources/{name}.mp3")
        pygame.mixer.Sound.play(sound)

    def play_background_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()

    def render_background(self):
        bg = pygame.image.load("resources/background.png")
        self.surface.blit(bg, (0, 0))

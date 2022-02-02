import pygame
import time
import settings
from pygame.locals import *
from .snake.snake import Snake
from .food import Food
from .leaderboard import LeaderBoard


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Py-Snake")

        pygame.mixer.init()
        self.play_background_music()

        self.surface = pygame.display.set_mode(settings.MAP_SIZE)
        self.surface.fill((0, 100, 0))
        self.snake = Snake(self.surface, 2)
        self.food = Food(self.surface)

        self.move_time = settings.MOVE_TIME

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
            self.move_time = self.move_time * 0.95

        # Snake collision with itself
        for i in range(0, self.snake.length - 1):
            if self.is_collision(self.snake.get_head_position(), self.snake.get_body_position(i)):
                self.die()

        # Snake outside walls
        x, y = self.snake.get_head_position()
        if x >= 1000 or x < 0 or y >= 800 or y < 0:
            self.die()

    def die(self):
        self.play_sound("crash")
        leaderboard = LeaderBoard(self.surface)
        leaderboard.save_score(self.snake.length)
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
        leader_board = LeaderBoard(self.surface)
        font = pygame.font.SysFont('arial', 30)

        self.surface.fill(settings.BACKGROUND_COLOR)

        place = leader_board.which_place(self.snake.length)
        line1 = font.render(
            f"Game is over! Your score is {self.snake.length}. You are TOP {place}", True, (255, 255, 255))
        self.surface.blit(line1, (200, 200))

        line2 = font.render(
            "To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (200, 250))

        leader_board.show()

        pygame.display.flip()

        pygame.mixer.music.pause()

    def reset(self):
        self.pause = False
        self.snake = Snake(self.surface, 2)
        self.food = Food(self.surface)
        pygame.mixer.music.unpause()
        self.move_time = settings.MOVE_TIME

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

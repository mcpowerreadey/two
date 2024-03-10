import pygame
import random

pygame.init()

# 游戏界面参数
screen_width = 800
screen_height = 600
block_size = 20
fps = 10

# 颜色定义
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# 初始化游戏界面
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('变态贪食蛇')

clock = pygame.time.Clock()

# 贪食蛇类
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width // 2), (screen_height // 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.color = green

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*block_size)) % screen_width), (cur[1] + (y*block_size)) % screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((screen_width // 2), (screen_height // 2))]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], block_size, block_size))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                if event.key == pygame.K_UP:
                    self.direction = (0, -1)
                if event.key == pygame.K_DOWN:
                    self.direction = (0, 1)
                if event.key == pygame.K_LEFT:
                    self.direction = (-1, 0)
                if event.key == pygame.K_RIGHT:
                    self.direction = (1, 0)

# 食物类
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = red
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, screen_width//block_size-1)*block_size, random.randint(0, screen_height//block_size-1)*block_size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], block_size, block_size))

# 初始化贪食蛇和食物
snake = Snake()
food = Food()

# 游戏循环
while True:
    screen.fill(black)

    snake.handle_keys()
    snake.move()
    snake.draw(screen)
    food.draw(screen)

    if snake.get_head_position() == food.position:
        snake.length += 1
        food.randomize_position()

    pygame.display.update()
    clock.tick(fps)

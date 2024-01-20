import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 设置屏幕大小和标题
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇游戏")

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# 定义贪吃蛇和食物的大小
snake_size = 20
food_size = 20

# 初始化贪吃蛇的位置和速度
snake = [(200, 200), (210, 200), (220, 200)]
snake_speed = (20, 0)

# 初始化食物的位置
food = (random.randrange(1, (width // food_size)) * food_size,
        random.randrange(1, (height // food_size)) * food_size)

# 初始化分数
score = 0

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_speed = (0, -snake_size)
    elif keys[pygame.K_DOWN]:
        snake_speed = (0, snake_size)
    elif keys[pygame.K_LEFT]:
        snake_speed = (-snake_size, 0)
    elif keys[pygame.K_RIGHT]:
        snake_speed = (snake_size, 0)

    # 移动贪吃蛇
    snake_head = (snake[0][0] + snake_speed[0], snake[0][1] + snake_speed[1])
    snake = [snake_head] + snake[:-1]

    # 检查是否吃到食物
    if snake[0] == food:
        score += 1
        food = (random.randrange(1, (width // food_size)) * food_size,
                random.randrange(1, (height // food_size)) * food_size)
        snake.append((0, 0))  # 在贪吃蛇尾部添加一个新的块

    # 检查是否碰到边界或自身
    if (snake[0][0] < 0 or snake[0][0] >= width or
            snake[0][1] < 0 or snake[0][1] >= height or
            snake[0] in snake[1:]):
        pygame.quit()
        sys.exit()

    # 清空屏幕
    screen.fill(black)

    # 画出贪吃蛇
    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], snake_size, snake_size))

    # 画出食物
    pygame.draw.rect(screen, red, (food[0], food[1], food_size, food_size))

    # 显示分数
    font = pygame.font.SysFont(None, 25)
    score_text = font.render("Score: {}".format(score), True, white)
    screen.blit(score_text, (10, 10))

    # 更新屏幕
    pygame.display.update()

    # 控制游戏速度
    pygame.time.Clock().tick(10)

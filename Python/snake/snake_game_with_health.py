import pygame
import sys
import random

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

# 初始化分数
score = 0

# 函数定义：初始化游戏
def init_game():
    global snake, snake_speed, health, food, score
    # 初始化贪吃蛇的位置、速度和生命值
    snake = [(200, 200), (210, 200), (220, 200)]
    snake_speed = (20, 0)
    health = 100  # 初始生命值

    # 初始化食物的位置
    food = (random.randrange(1, (width // food_size)) * food_size,
            random.randrange(1, (height // food_size)) * food_size)

    # 初始化分数
    score = 0

# 函数定义：绘制生命值条
def draw_health_bar():
    pygame.draw.rect(screen, (0, 255, 0), (10, 10, health, 10))

# 函数定义：绘制分数
def draw_score():
    font = pygame.font.SysFont(None, 25)
    score_text = font.render("Score: {}".format(score), True, white)
    screen.blit(score_text, (10, 30))

# 函数定义：检查碰撞
def check_collision():
    global health
    # 检查是否碰到边界
    if snake[0][0] < 0 or snake[0][0] >= width or snake[0][1] < 0 or snake[0][1] >= height:
        # 减少生命值
        health -= 20
        if health <= 0:
            return True  # 返回True表示游戏结束

        # 碰到墙壁后，远离墙壁
        if snake[0][0] < 0:
            snake[0] = (0, snake[0][1])
        elif snake[0][0] >= width:
            snake[0] = (width - snake_size, snake[0][1])
        elif snake[0][1] < 0:
            snake[0] = (snake[0][0], 0)
        elif snake[0][1] >= height:
            snake[0] = (snake[0][0], height - snake_size)

    # 检查是否碰到自身
    if snake[0] in snake[1:]:
        health -= 20
        if health <= 0:
            return True  # 返回True表示游戏结束

    return False

# 函数定义：运行游戏
def run_game():
    global snake, snake_speed, food, score, last_collision_time, last_collision_position, health

    # 记录上次碰撞的时间戳和位置
    last_collision_time = 0
    last_collision_position = snake[0]

    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    init_game()  # 按下空格键重新开始游戏

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
            health += 10  # 增加生命值
            if health > 100:
                health = 100
            food = (random.randrange(1, (width // food_size)) * food_size,
                    random.randrange(1, (height // food_size)) * food_size)
            snake.append((0, 0))

        # 检查碰撞
        if check_collision():
            # 如果游戏结束，初始化游戏
            init_game()

        # 清空屏幕
        screen.fill(black)

        # 画出贪吃蛇
        for segment in snake:
            pygame.draw.rect(screen, white, (segment[0], segment[1], snake_size, snake_size))

        # 画出食物
        pygame.draw.rect(screen, red, (food[0], food[1], food_size, food_size))

        # 绘制生命值条和分数
        draw_health_bar()
        draw_score()

        # 更新屏幕
        pygame.display.update()

        # 控制游戏速度
        pygame.time.Clock().tick(10)

# 显示开始提示
font = pygame.font.SysFont(None, 36)
start_text = font.render("Press SPACE to start", True, white)
screen.blit(start_text, (width // 4, height // 2))
pygame.display.update()

# 等待空格键按下开始游戏
waiting_for_start = True
while waiting_for_start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                waiting_for_start = False

# 初始化游戏
init_game()

# 运行游戏
run_game()

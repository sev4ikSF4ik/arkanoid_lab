import os
import time

code_chunks = [
    # 1
    "import pygame\nimport argparse\nimport sys\n\n",
    # 2
    "parser = argparse.ArgumentParser(description='Arkanoid Game')\nparser.add_argument('--speed', type=int, default=5, help='Скорость мяча')\nparser.add_argument('--bg', type=str, choices=['black', 'white'], default='black', help='Цвет фона')\nargs = parser.parse_args()\n\n",
    # 3
    "WIDTH, HEIGHT = 800, 600\nBG_COLOR = (0, 0, 0) if args.bg == 'black' else (255, 255, 255)\nPADDLE_COLOR = (0, 255, 0)\nBALL_COLOR = (255, 0, 0)\nBRICK_COLOR = (0, 0, 255)\n\npygame.init()\nscreen = pygame.display.set_mode((WIDTH, HEIGHT))\npygame.display.set_caption('Arkanoid CI/CD')\nclock = pygame.time.Clock()\n\n",
    # 4
    "class Paddle:\n    def __init__(self):\n        self.rect = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 40, 120, 15)\n    def draw(self):\n        pygame.draw.rect(screen, PADDLE_COLOR, self.rect)\n    def move(self, dx):\n        self.rect.x += dx\n        if self.rect.left < 0: self.rect.left = 0\n        if self.rect.right > WIDTH: self.rect.right = WIDTH\n\n",
    # 5
    "class Ball:\n    def __init__(self, speed):\n        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 15, 15)\n        self.dx = speed\n        self.dy = -speed\n    def draw(self):\n        pygame.draw.ellipse(screen, BALL_COLOR, self.rect)\n    def move(self):\n        self.rect.x += self.dx\n        self.rect.y += self.dy\n        if self.rect.left < 0 or self.rect.right > WIDTH:\n            self.dx *= -1\n        if self.rect.top < 0:\n            self.dy *= -1\n\n",
    # 6
    "paddle = Paddle()\nball = Ball(args.speed)\nbricks = [pygame.Rect(15 + i * 78, 20 + j * 35, 70, 25) for i in range(10) for j in range(5)]\n\n",
    # 7
    "while True:\n    for event in pygame.event.get():\n        if event.type == pygame.QUIT:\n            pygame.quit()\n            sys.exit()\n\n",
    # 8
    "    keys = pygame.key.get_pressed()\n    if keys[pygame.K_LEFT]: paddle.move(-8)\n    if keys[pygame.K_RIGHT]: paddle.move(8)\n    ball.move()\n\n",
    # 9
    "    if ball.rect.colliderect(paddle.rect) and ball.dy > 0: ball.dy *= -1\n    hit_index = ball.rect.collidelist(bricks)\n    if hit_index != -1:\n        hit_rect = bricks.pop(hit_index)\n        ball.dy *= -1\n\n",
    # 10
    "    if ball.rect.bottom > HEIGHT:\n        print('Game Over!')\n        pygame.quit()\n        sys.exit()\n    screen.fill(BG_COLOR)\n    paddle.draw()\n    ball.draw()\n    for b in bricks: pygame.draw.rect(screen, BRICK_COLOR, b)\n    pygame.display.flip()\n    clock.tick(60)\n"
]

commit_messages = [
    "Init base imports",
    "Add argparse for custom settings",
    "Setup Pygame window and constants",
    "Implement Paddle class",
    "Implement Ball class with physics",
    "Initialize game objects and bricks",
    "Add main game loop and exit event",
    "Add paddle and ball movement controls",
    "Implement collision detection",
    "Add game over logic and rendering"
]

os.system('git init')
os.system('git checkout -b feature-arkanoid')

# Очищаем файл перед стартом
with open('main.py', 'w', encoding='utf-8') as f:
    pass

for chunk, msg in zip(code_chunks, commit_messages):
    with open('main.py', 'a', encoding='utf-8') as f:
        f.write(chunk)
    os.system('git add main.py')
    os.system(f'git commit -m "{msg}"')
    time.sleep(1)

print("✅ Магия сработала! 10 коммитов в ветке feature-arkanoid созданы.")
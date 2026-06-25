import pygame
import argparse
import sys

parser = argparse.ArgumentParser(description='Arkanoid Game')
parser.add_argument('--speed', type=int, default=5, help='Скорость мяча')
parser.add_argument('--bg', type=str, choices=['black', 'white'], default='black', help='Цвет фона')
args = parser.parse_args()

WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 0, 0) if args.bg == 'black' else (255, 255, 255)
PADDLE_COLOR = (0, 255, 0)
BALL_COLOR = (255, 0, 0)
BRICK_COLOR = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Arkanoid CI/CD')
clock = pygame.time.Clock()

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 40, 120, 15)
    def draw(self):
        pygame.draw.rect(screen, PADDLE_COLOR, self.rect)
    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > WIDTH: self.rect.right = WIDTH


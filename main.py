import pygame
import argparse
import sys

parser = argparse.ArgumentParser(description='Arkanoid Game')
parser.add_argument('--speed', type=int, default=5, help='Скорость мяча')
parser.add_argument('--bg', type=str, choices=['black', 'white'], default='black', help='Цвет фона')
args = parser.parse_args()


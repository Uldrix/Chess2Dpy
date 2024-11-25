import pygame

def load_image(path):
    try:
        return pygame.image.load(path).convert_alpha()
    except pygame.error as e:
        raise FileNotFoundError(f"Image not found: {path}. Error: {e}")

def load_font(path, size):
    try:
        return pygame.font.Font(path, size)
    except pygame.error as e:
        raise FileNotFoundError(f"Font not found: {path}. Error: {e}")

import pygame
from game import Game

if __name__ == "__main__":
    pygame.init()
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pygame.quit()

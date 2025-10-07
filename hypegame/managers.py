import pygame
from pygame.locals import RESIZABLE

from .utils import _Singleton


class GameManager(metaclass=_Singleton):
    def __init__(
        self,
        title: str = "Hypegame Window",
        window_size: tuple[int, int] = (800, 500),
        is_resizable: bool = False,
    ):
        flags = RESIZABLE if is_resizable else 0

        pygame.init()

        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode(window_size, flags)

    def quit(self):
        pygame.quit()

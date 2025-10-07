from .managers import GameManager


def _get_screen():
    return GameManager().screen  # maybe not the best way to do it....

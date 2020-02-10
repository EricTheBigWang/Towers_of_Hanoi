import pygame

_screen_length = 400
_screen_height = 300
_screen = pygame.display.set_mode((_screen_length, _screen_height))


def height() -> int:
    """Return the height of the app screen.
    """
    return _screen_height


def length() -> int:
    """Return the length of the app screen.
    """
    return _screen_length


def get_screen() -> pygame.display:
    """Return the screen surface.
    """
    return _screen

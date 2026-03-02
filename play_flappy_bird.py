import os
import random
import sys
import pygame
from itertools import cycle
from pygame.locals import *

fps = 30
screen_width = 288
screen_height = 512
pipe_gap_size = 100
base_y = screen_height * 0.79
images, sounds, hitmasks = {}, {}, {}

PLAYERS_LIST = (
    # red box
    (
        'assets/sprites/redbox-upflap.png',
        'assets/sprites/redbox-midflap.png',
        'assets/sprites/redbox-downflap.png',
    ),
    # blue box
    (
        'assets/sprites/bluebox-upflap.png',
        'assets/sprites/bluebox-midflap.png',
        'assets/sprites/bluebox-downflap.png',
    ),
    # yellow box
    (
        'assets/sprites/yellowbox-upflap.png',
        'assets/sprites/yellowbox-midflap.png',
        'assets/sprites/yellowbox-downflap.png',
    ),
)

# list of backgrounds
BACKGROUNDS_LIST = (
    'assets/sprites/background-day.png',
    'assets/sprites/background-night.png',
)

# list of pipes
PIPES_LIST = (
    'assets/sprites/pipe-green.png',
    'assets/sprites/pipe-red.png',
)
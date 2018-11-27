import pygame
from pygame import *

import logic


krister = logic.Player(100000)

print(krister.get_money())
krister.decrease_money(1000)

print(krister.get_money())








# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

from os.path import join
import pygame
from pygame.locals import *
from simulation.car import Car


def load_image(name, colorkey=None):
    fullname = join('res', 'img', name)
    #print(fullname)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def handle_input():
    """ Handle Input Events """
    for event in pygame.event.get():
        if event.type == QUIT:
            return True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            return True
        elif event.type == MOUSEBUTTONDOWN:
            print("Mouse down")
        elif event.type is MOUSEBUTTONUP:
            print("Mouse up")


def load_cars():
    params1 = {}
    params2 = {
                'routes': {
                    'route_size': 2,
                    'route': [
                        [1, 2, 0, 0],
                        [3, 1, 0, 0]
                    ]
                }
              }
    params2 = {
                #'position': [10, 10],
                'angle': 0
              }
    car1 = Car("Carro 1", params1)
    car2 = Car("Carro 2", params2)
    return [car1, car2]

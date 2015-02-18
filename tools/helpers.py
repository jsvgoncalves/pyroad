# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

from os.path import join
import pygame
from pygame.locals import *
from simulation.car import Car

CONFIG_DIR = 'config'

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


def load_configs(file_path):
    """Returns list of cars

    Loads all the configurations from the give file_path.
    Should in the future return multiple configs (not only cars).
    """
    import json
    import os.path as osp

    file_full_path = osp.join(CONFIG_DIR, file_path)
    with open(file_full_path) as data_file:
        data = json.load(data_file)
        # General configs
        pass
        # Cars
        cars = [load_car(car) for car in data['cars'] if data['cars']]

    return cars


def load_car(car_json):
    car = Car("Carro 1", car_json)
    return car

# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.
import pygame
from gui.helpers import load_image
from time import sleep


class CarSprite(pygame.sprite.Sprite):
    """CarSprite used on pygame GUI"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.image, self.rect = load_image('chimp.bmp', -1)
        screen = pygame.display.get_surface()
        # The current screen area
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move_x = 9
        self.move_y = 9

    def update(self, move_x, move_y):
        # Just moves the car from one side to the other
        # rect.move(x_offset, y_offset)
        self.rect = self.rect.move((move_x, move_y))


class Car():
    """Basic car model"""
    def __init__(self, name):
        self.speed = [0, 1]
        self.pos = [0, 0]
        self.name = name
        self.sprite = CarSprite()

    def get_sprite(self):
        return self.sprite

    def update(self):
        "physics forces update"
        print(self.pos)
        sleep(0.1)
        if self.speed[0] < 3:
            self.speed[0] += 1
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

        # Updates the sprite of the car.
        self.sprite.update(self.pos[0], self.pos[1])

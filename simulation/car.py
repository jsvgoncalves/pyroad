# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.
import pygame
from gui.helpers import load_image
#from time import sleep


class CarSprite(pygame.sprite.Sprite):
    """CarSprite used on pygame GUI"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.image, self.rect = load_image('chimp.bmp', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move = 9

    def update(self):
        # Just moves the car from one side to the other
        newpos = self.rect.move((self.move, 0))
        if self.rect.left < self.area.left or \
           self.rect.right > self.area.right:
            self.move = -self.move
            newpos = self.rect.move((self.move, 0))
            self.image = pygame.transform.flip(self.image, 1, 0)
        self.rect = newpos


class Car():
    """Basic car model"""
    def __init__(self, name):
        self.speed = 0
        self.name = name
        self.sprite = CarSprite()

    def get_sprite(self):
        return self.sprite

    def update(self):
        "physics forces update"
        if self.speed < 15:
            self.speed += 1

        # Updates the sprite of the car.
        self.sprite.update()
        print(self.name, self.speed)

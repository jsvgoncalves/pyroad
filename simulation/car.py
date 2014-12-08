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

    def update(self, move_x, move_y):
        # Just moves the car from one side to the other
        # rect.move(x_offset, y_offset)
        self.rect = self.rect.move((move_x, move_y))


class Car():
    """Basic car model
       Car effectors:
        - acceleration pedal [0..1]
        - brake pedal [0..1]
        - steering wheel [-1..1]
    """

    def __init__(self, name, velocity_x, velocity_y):
        self.name = name
        self.sprite = CarSprite()

        # Init car state
        self.velocity = [velocity_x, velocity_y]
        self.pos = [0, 0]

        # Init effectors state
        self.acceleration = 0
        self.brake = 0
        self.steering = 0

    def get_sprite(self):
        return self.sprite

    def set_sensors(self, sensor_data):
        """Inputs the data from the sensors"""
        return

    def update(self, delta_seconds):
        """physics forces update"""
        #print(self.pos)
        sleep(0.1)
        self.pos[0] += self.velocity[0] * delta_seconds
        self.pos[1] += self.velocity[1] * delta_seconds

        # Updates the sprite of the car.
        self.sprite.update(self.pos[0], self.pos[1])

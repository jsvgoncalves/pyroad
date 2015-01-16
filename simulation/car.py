# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

import tools.helpers
import pygame
#from time import sleep
GUI_SCALE = 2


class CarSprite(pygame.sprite.Sprite):
    """CarSprite used on pygame GUI"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.image, self.rect = tools.helpers.load_image('car.png', -1)

    def update(self, move_x, move_y):
        # Just moves the car from one side to the other
        # rect.move(x_offset, y_offset)
        self.rect = self.rect.move((GUI_SCALE * move_x,
                                    GUI_SCALE * move_y))
        #self.rect = rot_center()

    def rot_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image, rot_rect


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
        self.position = [0, 0]
        self.delta_pos = [0, 0]  # Unused
        self.angle = 0.71  # rad

        # Init effectors state
        self.acceleration_pedal = 0.1  # 0..1
        self.brake_pedal = 0  # 0..1
        self.steering = 1  # -1..1

        # Car characterics
        # self.max_turning_angle = ~ 8m radius
        self.max_steering_angle = 0.785398163  # 45 deg
        # search ac 1g
        self.max_acceleration = 3  # m/s^2
        self.max_decceleration = -10  # m/s^2  ( usually -4 )
        #self.engine_power = 10  # Maybe later..

    def get_sprite(self):
        return self.sprite

    def set_sensors(self, sensor_data):
        """Inputs the data from the sensors
            _angle - [-pi, pi] angle between car direction and xx axis
            angle  - [-pi, pi] angle between car direction and track axis
            opponents_dist - [0,100]x18 sliced
            speed_x -
            speed_y -
            track_edges_dist - [0,100]x18 sliced
            track_axis_dist -
        """
        return

    def update(self, new_position):
        """physics forces update"""
        # Updates car geo variables
        self.position = new_position
        # Updates the sprite of the car.
        self.sprite.update(self.position[0], self.position[1])

    def get_effectors(self):
        """ sends the effectors back to the simulation engine """
        return self.acceleration_pedal

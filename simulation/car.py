# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

import tools.helpers
import pygame
from math import degrees

#from time import sleep
GUI_SCALE = 1


class CarSprite(pygame.sprite.Sprite):
    """CarSprite used on pygame GUI"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.master_image, self.rect = tools.helpers.load_image('car.png', -1)
        self.image = self.master_image

    def update(self, move_x, move_y, current_angle):
        # Just moves the car from one side to the other
        # rect.move(x_offset, y_offset)
        self.rect = self.rect.move(0, 0)
        self.rect = self.rect.move((GUI_SCALE * move_x,
                                    GUI_SCALE * move_y))
        self.rot_center(-degrees(current_angle))

    def rot_center(self, angle):
        """rotate a Surface, maintaining position."""
        retaining_center = self.rect.center
        self.image = pygame.transform.rotate(self.master_image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = retaining_center


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
        #self.velocity = [velocity_x, velocity_y]
        self.velocity = [0, 0]
        self.position = [0, 0]
        self.delta_pos = [0, 0]  # Unused
        #self.angle = 0.71  # rad
        self.angle = 0.0  # rad

        # Init effectors state
        self.acceleration_pedal = 0.4  # 0..1
        self.brake_pedal = 0  # 0..1
        self.steering = 0  # -1..1

        # Car characterics
        # self.max_turning_angle = ~ 8m radius
        self.max_steering_angle = 0.785398163  # 45 deg
        # search ac 1g
        self.max_acceleration = 3  # m/s^2
        self.max_decceleration = -10  # m/s^2  ( usually -4 )
        #self.engine_power = 10  # Maybe later..

        self.width = [2, 2]  # [left, right] from center
        self.height = [3, 4]  # [back, front] from center

        # Physical dimensions of the cars
        self.width = [2, 2]  # [left, right] from the center of the car
        self.length = [4, 5]  # [back, front] from the center of the car

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
        self._angle = sensor_data['_angle']
        self.angle = sensor_data['angle']
        self.opponents_dist = sensor_data['opponents_dist']
        self.speed = sensor_data['speed']
        self.acceleration = sensor_data['acceleration']
        self.track_edges_dist = sensor_data['track_edges_dist']
        self.track_axis_dist = sensor_data['track_axis_dist']
        return

    def update(self, new_position):
        """physics forces update"""
        # Updates car geo variables
        self.steering = 0.002
        # if angle > 360
        if self.angle >= 6.28318531:
            self.angle = 0
        elif self.angle <= -6.28318531:
            self.angle = 0

        # Updates the sprite of the car.
        self.sprite.update(new_position[0],
                           new_position[1],
                           self.angle)

        self.position = new_position
        print("self.position[0], self.position[1], self.angle")
        print(self.position[0],
              self.position[1],
              self.angle)

    def get_effectors(self):
        """ sends the effectors back to the simulation engine """
        return self.acceleration_pedal, self.brake_pedal, self.steering

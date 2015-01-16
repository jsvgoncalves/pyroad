# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.
from tools.helpers import load_cars
import math


class SimulationState():
    """moves a clenched fist on the screen, following the mouse"""
    def __init__(self):
        # Vehicles in the simulation
        self.cars = load_cars()

    def get_sprites(self):
        sprites = []
        for car in self.cars:
            sprites.append(car.get_sprite())
        return sprites
        #return self.cars[0].get_sprite()

    def update(self, delta_seconds):
        "simulation objects update"

        # Update vehicles
        # Maybe it would be best to request intentions from cars
        # And use physics engine, calculate new car state,
        # And give it back to the car

        acceleration = (self.cars[0].get_effectors() *
                        self.cars[0].max_acceleration)
        car_angle = self.cars[0].angle

        '''Physics
        Should be extracted and improved.
        '''
        accel_vect = [0, 0]
        accel_vect[0] = acceleration * math.cos(car_angle)
        accel_vect[1] = acceleration * math.sin(car_angle)
        #  Multiply by elapsed time to get delta_accel
        delta_accel = [i * delta_seconds for i in accel_vect]

        # Update position
        position = [0, 0]  # tmp var
        position[0] = self.cars[0].position[0] + delta_accel[0]
        position[1] = self.cars[0].position[1] + delta_accel[1]
        self.cars[0].update(position)

        #self.cars[1].get_effectors()
        #self.cars[0].update(delta_seconds)
        #self.cars[1].update(delta_seconds)

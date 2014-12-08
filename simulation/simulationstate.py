# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.
from tools.helpers import load_cars


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
        self.cars[0].update(delta_seconds)
        self.cars[1].update(delta_seconds)

# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.
from car import Car


class SimulationState():
    """moves a clenched fist on the screen, following the mouse"""
    def __init__(self):
        # Vehicles in the simulation
        self.car1 = Car("Carro 1")
        self.car2 = Car("Carro 2")

    def get_sprites(self):
        return self.car1.get_sprite()

    def update(self):
        "simulation objects update"
        # Update vehicles
        self.car1.update()
        self.car2.update()

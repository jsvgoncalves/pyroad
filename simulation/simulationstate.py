# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.
from tools.helpers import load_cars
import math


class SimulationState():
    """Data structure of simulation state.
    Also responsible for bridging the vehicles with the physics engine.
    """
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

        car = self.cars[0]
        # acceleration pedal * max acceleration
        acel_pedal, brake_pedal, steering = car.get_effectors()
        acceleration = (acel_pedal *
                        car.max_acceleration)
        #print("acel_pedal, acceleration")
        #print(acel_pedal, acceleration)
        # Update car angle
        angle_changed = car.max_steering_angle * steering

        car_angle = car.angle + angle_changed
        car.angle = car_angle
        #print("steering, angle_changed")
        #print(steering, angle_changed)

        '''Physics
        Should be extracted and improved.
        '''
        accel_vect = [0, 0]
        accel_vect[0] = acceleration * math.cos(car_angle)
        accel_vect[1] = acceleration * math.sin(car_angle)
        #  Multiply by elapsed time to get delta_accel
        #print("################\n")
        #print("acel_x, acel_y")
        #print(accel_vect[0], accel_vect[1])
        #print("")
        delta_accel = [i * delta_seconds for i in accel_vect]

        #print("deltaacel_x, deltaacel_y")
        #print(delta_accel[0], delta_accel[1])
        #print("")
        # Update velocity
        velocity = [0, 0]  # tmp var
        velocity[0] = car.velocity[0] + delta_accel[0]
        velocity[1] = car.velocity[1] + delta_accel[1]
        # Should control max velocity too

        #print("vel_x, vel_y")
        #print(velocity[0], velocity[1])
        #print("")
        # Update position
        position = [0, 0]  # tmp var
        #position[0] = car.position[0] + delta_accel[0]
        #position[1] = car.position[1] + delta_accel[1]

        position[0] = car.position[0] + velocity[0]
        position[1] = car.position[1] + velocity[1]

        car.update(position)

        #self.cars[1].get_effectors()
        #self.cars[0].update(delta_seconds)
        #self.cars[1].update(delta_seconds)

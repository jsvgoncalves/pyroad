# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.
from tools.helpers import load_configs
import math

#CONFIG_FILE = 'pyroad.json'
CONFIG_FILE = 'pyroad-2.json'


class SimulationState():
    """Data structure of simulation state.
    Also responsible for bridging the vehicles with the physics engine.
    """
    def __init__(self):
        # Vehicles in the simulation
        self.cars = load_configs(CONFIG_FILE)
        self.elapsed_time = 0

    def get_sprites(self):
        sprites = []
        for car in self.cars:
            sprites.append(car.get_sprite())
        return sprites
        # return self.cars[0].get_sprite()

    def update(self, delta_seconds):
        "simulation objects update"

        # Update vehicles
        # Maybe it would be best to request intentions from cars
        # And use physics engine, calculate new car state,
        # And give it back to the car
        for car in self.cars:
            # acceleration pedal * max aceleration
            acel_pedal, brake_pedal, steering = car.get_effectors()
            acceleration = (acel_pedal *
                            car.max_acceleration)
            # Brake pedal
            acceleration = acceleration * (1 - brake_pedal)
            # print("acel_pedal, aceleration")
            # print(acel_pedal, acceleration)
            # Update car angle
            angle_changed = car.max_steering_angle * steering

            car_angle = car.angle + angle_changed
            car.angle = car_angle
            # print("steering, angle_changed")
            # print(steering, angle_changed)

            '''Physics
            Should be extracted and improved.
            '''
            accel_vect = [0, 0]
            accel_vect[0] = acceleration * math.cos(car_angle)
            accel_vect[1] = acceleration * math.sin(car_angle)
            # Multiply by elapsed time to get delta_accel
            # print("################\n")
            # print("acel_x, acel_y")
            # print(accel_vect[0], accel_vect[1])
            # print("")
            delta_accel = [i * delta_seconds for i in accel_vect]

            # print("deltaacel_x, deltaacel_y")
            # print(delta_accel[0], delta_accel[1])
            # print("")
            # Update velocity
            velocity = [0, 0]  # tmp var
            velocity[0] = car.velocity[0] + delta_accel[0]
            velocity[1] = car.velocity[1] + delta_accel[1]
            # Should control max velocity too

            ### TEMP
            if acceleration == 0:
                #print("0 Accel")
                velocity = [0, 0]
            ###

            # print("vel_x, vel_y")
            # print(velocity[0], velocity[1])
            # print("")
            # Update position
            position = [0, 0]  # tmp var
            # position[0] = car.position[0] + delta_accel[0]
            # position[1] = car.position[1] + delta_accel[1]

            position[0] = car.position[0] + velocity[0]
            position[1] = car.position[1] + velocity[1]

            car.update(position)

            self.elapsed_time += delta_seconds
            sensor_data = {'elapsed_time': self.elapsed_time}
            car.set_sensors(sensor_data)
            # self.cars[1].get_effectors()
            # self.cars[0].update(delta_seconds)
            # self.cars[1].update(delta_seconds)

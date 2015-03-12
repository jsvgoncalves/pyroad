# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

# import tools.helpers
# import pygame
# from math import degrees

# from time import sleep


class Car():
    """Basic car model
       Car effectors:
        - acceleration pedal [0..1]
        - brake pedal [0..1]
        - steering wheel [-1..1]
    """

    def __init__(self, name, init_params):
        self.name = name

        # Init car state
        self.velocity = [0, 0]
        self.position = [0, 0]
        self.delta_pos = [0, 0]  # Unused
        self.angle = 1.0471975511965976  # rad
        # self.angle = 0.0  # rad

        # Init effectors state
        self.acceleration_pedal = 0.4  # 0..1
        self.brake_pedal = 0  # 0..1
        self.steering = 0  # -1..1

        # Car characterics
        # self.max_turning_angle = ~ 8m radius
        self.max_steering_angle = 0.7853981633974483  # 45 deg
        # search ac 1g
        self.max_acceleration = 3  # m/s^2
        self.max_decceleration = -10  # m/s^2  ( usually -4 )
        # self.engine_power = 10  # Maybe later..

        # Physical dimensions of the cars
        self.width = [2, 2]  # [left, right] from the center of the car
        self.length = [4, 5]  # [back, front] from the center of the car

        # From parameters
        if 'position' in init_params:
            self.position = init_params['position']

        if 'angle' in init_params:
            self.angle = init_params['angle']

        # Routes (Intention/Plan) for the car
        self.route = []
        self.current_route = 0

        if 'routes' in init_params:
            self.route = init_params['routes']['route']
            self.route_size = init_params['routes']['route_size'] - 1
            self.has_routes = True
        else:
            self.has_routes = False

        self.elapsed_time = 0

    def set_sensors(self, sensor_data):
        """Inputs the data from the sensors
            _angle - [-pi, pi] angle between car direction and xx axis
            angle  - [-pi, pi] angle between car direction and track axis
            opponents_dist - [0,100]x18 sliced
            speed_x -
            speed_y -
            track_edges_dist - [0,100]x18 sliced
            track_axis_dist -
            elapsed_time - elapsed_time since simulation start
        """
        # self._angle = sensor_data['_angle']
        # self.angle = sensor_data['angle']
        # self.opponents_dist = sensor_data['opponents_dist']
        # self.speed = sensor_data['speed']
        # self.acceleration = sensor_data['acceleration']
        # self.track_edges_dist = sensor_data['track_edges_dist']
        # self.track_axis_dist = sensor_data['track_axis_dist']
        self.elapsed_time = sensor_data['elapsed_time']

    def update(self, new_position, new_angle):
        """physics forces update"""
        # Updates car geo variables
        # self.steering = 0.002
        # if angle > 360
        # assert(self.angle >= 6.28318531), "angle too big"
        # assert(self.angle <= -6.28318531), "angle too small"
#        if self.angle >= 6.28318531:
#            self.angle = 0
#        elif self.angle <= -6.28318531:
#            self.angle = 0

        self.position = new_position
        self.angle = new_angle
        # print("self.position[0], self.position[1], self.angle")
        # print(self.position[0],
        #       self.position[1],
        #       self.angle)

        if self.has_routes:
            if self.elapsed_time >= self.route[self.current_route][0]:
                self.steering = self.route[self.current_route][1]
                self.acceleration_pedal = self.route[self.current_route][2]
                self.brake_pedal = self.route[self.current_route][3]
                if self.current_route < self.route_size:
                    self.current_route += 1
        else:
            pass

    def get_effectors(self):
        """ sends the effectors back to the simulation engine """
        return self.acceleration_pedal, self.brake_pedal, self.steering

    def get_name(self):
        return self.name

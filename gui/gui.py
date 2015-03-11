# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.
import pygame
from pygame.locals import *
import datetime
from math import degrees
from tools.helpers import handle_input
from tools.helpers import load_image


GUI_UPDATE_SECONDS = 0.05
GUI_SCALE = 100


class Gui():
    """Modular GUI"""
    def __init__(self, simulation_looper):
        self.sim = simulation_looper
        # self.init_pygame()

    def init_pygame(self):
        # Initialize Everything
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('PyRoad')
        pygame.mouse.set_visible(0)

        # Create The Backgound
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((80, 100, 60))

        # Display The self.Background
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        # Prepare Game Objects
        self.clock = pygame.time.Clock()
        self.allsprites = pygame.sprite.RenderPlain()

        self.add_sprites()

    def add_sprites(self):
        """ Adds sprites to the allsprites object"""
        self.car_sprites = {}
        self.cars = self.sim.get_state().cars
        for car in self.cars:
            self.car_sprites[car.name] = CarSprite()
        # self.car_sprites = []
        # for car in cars:
        #     self.car_sprites.append(CarSprite())
        self.allsprites = pygame.sprite.RenderPlain(self.car_sprites.values())

    def update(self):
        """update"""

        for car in self.sim.get_state().cars:
            # pass
            self.car_sprites[car.name].update(car.position[0],
                                             car.position[1],
                                             car.angle)
        # self.update_car(car, delta_seconds)
        # self.sprite.update(new_position[0],
        #            new_position[1],
        #            self.angle)
        self.screen.blit(self.background, (0, 0))
        self.allsprites.draw(self.screen)
        pygame.display.flip()

    def run(self):
        # GUI
        # Extrair para thread
        self.init_pygame()
        previous_time = datetime.datetime.now()
        pygame.init()
        while True:
            current_time = datetime.datetime.now()
           # print("#gui")
           # print(current_time)
            # print("#sim")
            # print(self.sim.previous_time)

            # Handle imput
            simulation_is_ending = handle_input()

            time_diff = current_time - previous_time
            if(time_diff.total_seconds() > GUI_UPDATE_SECONDS):
                self.update()
               # print("#update")
               # print(datetime.datetime.now())

                previous_time = current_time

            # Exiting
            if simulation_is_ending:
                return


class CarSprite(pygame.sprite.Sprite):
    """CarSprite used on pygame GUI"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.master_image, self.rect = load_image('car.png', -1)
        self.image = self.master_image
        self.previous = [0, 0]

    def update(self, delta_x, delta_y, current_angle):
        # Just moves the car from one side to the other
        # rect.move(x_offset, y_offset)
        #self.rect.center = (GUI_SCALE * move_x, GUI_SCALE * move_y)
        # Move to origin
        self.rect.move_ip((-GUI_SCALE * self.previous[0],
                           -GUI_SCALE * self.previous[1]))
        # Move to new position
        self.rect.move_ip((GUI_SCALE * delta_x,
                           GUI_SCALE * delta_y))
        # Rotate
        self.rot_center(-degrees(current_angle))
        # Update position meta
        self.previous = (delta_x, delta_y)

    def rot_center(self, angle):
        """rotate a Surface, maintaining position."""
        retaining_center = self.rect.center
        self.image = pygame.transform.rotate(self.master_image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = retaining_center

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
        # self.init_pygame()  # Moved to the run for threading reasons.

    def init_pygame(self):
        # Initialize the engine and the display
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
        # Cars sprites are in a dict for easy and constant-access time
        self.car_sprites = {}
        for car in self.sim.get_state().cars:
            self.car_sprites[car.name] = CarSprite()
        # Add the values of the dict to the allsprites object
        # which is used for rendering
        self.allsprites = pygame.sprite.RenderPlain(self.car_sprites.values())

    def update(self):
        """Updates the model data and redraws the scene accordingly."""
        self.update_vehicle_info()
        self.update_pygame_render()

    def update_vehicle_info(self):
        """Update the sprite of each car"""
        for car in self.sim.get_state().cars:
            self.car_sprites[car.name].update(car.position[0],
                                              car.position[1],
                                              car.angle)

    def update_pygame_render(self):
        """Pygame rendering updates"""
        # Blit the background into the screen
        self.screen.blit(self.background, (0, 0))
        # Draw car sprites
        self.allsprites.draw(self.screen)
        # Flip the display (double-buffering)
        pygame.display.flip()

    def run(self):
        """Main GUI Loop"""
        # Initializes Pygame engine.
        # Dislocated from Gui.__init__() for threading reasons.
        self.init_pygame()
        # Creat the datetime for maximizing update rate.
        previous_time = datetime.datetime.now()
        while True:
            current_time = datetime.datetime.now()

            # Handle imput
            simulation_is_ending = handle_input()

            time_diff = current_time - previous_time
            if(time_diff.total_seconds() > GUI_UPDATE_SECONDS):
                self.update()
                previous_time = current_time

            # Exiting
            if simulation_is_ending:
                return


class CarSprite(pygame.sprite.Sprite):
    """CarSprite used on pygame GUI"""
    def __init__(self, sprite='car.bmp'):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.master_image, self.rect = load_image(sprite, -1)
        self.image = self.master_image
        self.previous = [0, 0]

    def update(self, pos_x, pos_y, current_angle):
        """Update vehicle coordinates and angle."""
        # Firstly move the sprite to the origin
        self.rect.move_ip((-GUI_SCALE * self.previous[0],
                           -GUI_SCALE * self.previous[1]))
        # Then move it to the new position
        self.rect.move_ip((GUI_SCALE * pos_x,
                           GUI_SCALE * pos_y))
        # Rotate accordingly
        self.rot_center(-degrees(current_angle))
        # Update position meta
        self.previous = (pos_x, pos_y)

    def rot_center(self, angle):
        """Rotate a Surface, maintaining position."""
        retaining_center = self.rect.center
        self.image = pygame.transform.rotate(self.master_image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = retaining_center

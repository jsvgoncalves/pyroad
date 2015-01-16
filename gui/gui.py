# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.
import pygame
from pygame.locals import *


class Gui():
    """Modular GUI"""
    def __init__(self):
        #Initialize Everything
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption('PyRoad')
        pygame.mouse.set_visible(0)

        #Create The Backgound
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((80, 100, 60))

        #Display The self.Background
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        #Prepare Game Objects
        self.clock = pygame.time.Clock()
        self.allsprites = pygame.sprite.RenderPlain()

    def add_sprites(self, sprites):
        """ Adds sprites to the allsprites object"""
        self.allsprites = pygame.sprite.RenderPlain(sprites)

    def update(self):
        "update"
        self.screen.blit(self.background, (0, 0))
        self.allsprites.draw(self.screen)
        pygame.display.flip()

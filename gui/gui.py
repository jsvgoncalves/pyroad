# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.
import pygame
from pygame.locals import *


class Gui():
    """moves a clenched fist on the self, following the mouse"""
    def __init__(self):
        #Initialize Everything
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Monkey Fever')
        pygame.mouse.set_visible(0)

        #Create The Backgound
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((80, 100, 60))

        #Put Text On The self.Background, Centered
        if pygame.font:
            font = pygame.font.Font(None, 36)
            # = font.render("Pummel The Chimp, And Win $$$", 1,
            #                   (10, 10, 10))
            #textpos = text.get_rect(centerx=self.background.get_width()/2)
            #self.background.blit(text, textpos)
            #self.background.blit(text, textpos)

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

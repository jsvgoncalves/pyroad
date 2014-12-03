# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.
from simulationstate import SimulationState
from gui.helpers import handle_input


class SimulationLooper():
    """moves a clenched fist on the screen, following the mouse"""
    def __init__(self, name, gui):
        self.gui = gui
        self.simulation = SimulationState()
        sprites = self.simulation.get_sprites()
        self.gui.add_sprites(sprites)

    def run(self):
        "simulation objects update"
        # Main Loop
        while 1:
            # gui.clock.tick(60)  # !FIXME: Shouldn't be dependent on GUI
            simulation_is_ending = handle_input()
            self.simulation.update()
            self.gui.update()
            if simulation_is_ending:
                return

# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.
from simulationstate import SimulationState
from gui.helpers import handle_input
import datetime


class SimulationLooper():
    """Simulation Core with looper and top-level objects"""

    def __init__(self, name, gui):
        # Init Simulation model
        self.simulation = SimulationState()

        # Add the sprites from the current simulation to the GUI
        sprites = self.simulation.get_sprites()
        self.gui = gui
        self.gui.add_sprites(sprites)

    def run(self):
        "simulation objects update"
        a = datetime.datetime.now()
        # Main Loop
        while 1:
            # gui.clock.tick(60)  # !FIXME: Shouldn't be dependent on GUI
            b = datetime.datetime.now()
            c = b - a
            a = b
            #print(c.total_seconds())

            # Inputs
            simulation_is_ending = handle_input()

            # Model updates
            self.simulation.update(c.total_seconds())

            # GUI
            self.gui.update()

            # Exiting
            if simulation_is_ending:
                return

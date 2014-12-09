# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.
from simulationstate import SimulationState
from tools.helpers import handle_input
import datetime

PHYSICS_UPDATE_SECONDS = 0.05
GUI_UPDATE_SECONDS = 0.05

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
        previous_time = datetime.datetime.now()
        last_update_gui = previous_time
        # Main Loop
        while 1:
            # gui.clock.tick(60)  # !FIXME: Shouldn't be dependent on GUI
            current_time = datetime.datetime.now()
            time_diff = current_time - previous_time
            #print(time_diff.total_seconds())

            # Inputs
            simulation_is_ending = handle_input()

            # Model updates
            if(time_diff.total_seconds() > PHYSICS_UPDATE_SECONDS):
                self.simulation.update(time_diff.total_seconds())
                previous_time = current_time

            # GUI
            gui_time_diff = current_time - last_update_gui
            #print(gui_time_diff.total_seconds())

            if(gui_time_diff.total_seconds() > GUI_UPDATE_SECONDS):
                self.gui.update()
                last_update_gui = current_time

            # Exiting
            if simulation_is_ending:
                return

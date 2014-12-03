# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

from __future__ import print_function
from gui.gui import Gui
from pygame.locals import *
from simulation.simulationlooper import SimulationLooper


def main():
    # Launch a GUI
    gui = Gui()

    # Initialize simulation looper
    sim = SimulationLooper("Simulation One", gui)
    sim.run()

    # Finish and clean up
    print("Simulation stopped.")

if __name__ == '__main__':
    main()

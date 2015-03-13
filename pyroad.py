# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

from __future__ import print_function
from Queue import Queue
import threading
from pygame.locals import *

# event_queue = []
from simulation.simulationlooper import SimulationLooper
from gui.gui import Gui
from server import pyroad_twisted as ts
q = Queue()


def main():

    # Initialize simulation looper
    sim = SimulationLooper("Simulation One")
    sim_t = threading.Thread(target=sim.run, args=(q,))
    sim_t.daemon = True
    sim_t.start()

    # Create a GUI instance
    gui = Gui(sim)
    gui_t = threading.Thread(target=gui.run)
    gui_t.daemon = True
    gui_t.start()

    # Start the Twisted Server
    ts.start(q, sim)

    # Finish and clean up
    print("Simulation stopped.")

if __name__ == '__main__':
    main()

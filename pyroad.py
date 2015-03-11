# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

from __future__ import print_function
from gui.gui import Gui
from pygame.locals import *
from simulation.simulationlooper import SimulationLooper

from multiprocessing import Process
from multiprocessing import Queue
import threading
# event_queue = []


from twisted.internet import protocol, reactor, endpoints


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

# a = 1
def main():
    #q = Queue()

    # Initialize simulation looper
    sim = SimulationLooper("Simulation One")
    sim_t = threading.Thread(target=sim.run)
    #sim_t.daemon = True
    sim_t.start()

    # Create a GUI instance
    gui = Gui(sim)
    gui_t = threading.Thread(target=gui.run)
    #gui_t.daemon = True
    gui_t.start()

    # Start the Twisted Server
    endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
    reactor.run()

    # Finish and clean up
    print("Simulation stopped.")

if __name__ == '__main__':
    main()

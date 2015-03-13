# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

from twisted.internet import protocol, reactor, endpoints
import json


class VehicleControl(protocol.Protocol):
    def __init__(self, factory, addr, q):
        self.factory = factory
        # Save the sim_state in a var for access-performance reasons
        self.sim_state = self.factory.sim.simulation
        self.addr = addr
        self.q = q

    def connectionMade(self):
        self.transport.write("Thank you for connecting\r\n")
        print("connectionMade")
        print(self.addr)
        # self.transport.loseConnection()

    def connectionLost(self, reason):
        print("connectionLost")
        print(reason)

    def dataReceived(self, data):
        # print(dir(data))
        # print(str(self.addr) + ": " + data)
        try:
            formatted_data = json.loads(data)
            formatted_data['client_id'] = self.addr

            # Send the simulation status back to the client
            # Check if the simulation step has changed
            if self.sim_state.sim_step > self.factory.sim_step:
                self.factory.sim_step = self.sim_state.sim_step
                new_rep = {'cars': {}}
                for car in self.sim_state.cars:
                    new_rep['cars'][car.name] = car.position
                self.factory.sim_rep = json.dumps(new_rep)
            # If it did, format it and save it in Factory
            self.q.put(formatted_data)
            self.transport.write(self.factory.sim_rep)
        except ValueError:
            self.transport.write("Invalid message")


class VehicleControlFactory(protocol.Factory):
    def __init__(self, q, sim_loop):
        self.q = q
        self.sim = sim_loop
        # Representation of the simulation state (to send to clients)
        self.sim_rep = {}
        self.sim_step = self.sim.simulation.sim_step

    def buildProtocol(self, addr):
        return VehicleControl(self, addr, self.q)


def start(q, sim_loop):
    """Starts and runs the server connecting the Factory to the endpoint.

    It is a blocking run.
    """
    endpoints.serverFromString(
        reactor, "tcp:9001").listen(
            VehicleControlFactory(q, sim_loop))
    reactor.run()

# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

from simulationstate import SimulationState
import Queue
import datetime
# from tools.helpers import ClientInput

PHYSICS_UPDATE_SECONDS = 0.01


class SimulationLooper():
    """Simulation Core with looper and top-level objects"""

    def __init__(self, name):
        # Init Simulation model
        self.simulation = SimulationState()

    def run(self, q):
        """Simulation objects update.

        Runs indefinitely, calling simulationstate.update() with a maximum
        cadence of PHYSICS_UPDATE_SECONDS.
        Parses the clients' inputs from a Queue as soon as they arrive.

        Args:
            q (Queue): The queue with clients' inputs.
        """
        self.previous_time = datetime.datetime.now()

        # Main Loop
        while True:
            current_time = datetime.datetime.now()
            # print("#sim")
            # Inputs
            inputs = self.check_clients_input(q)
            for c_i in inputs:
                # print(c_i)
                for k, v in c_i.iteritems():
                    print(str(k) + " : " + str(v))
            # simulation_is_ending = handle_input()
            # (timestamp, effectors)
            # client_events = [ev_1, ..., ev_n]
            # Objecto com o input dos carros por TCP
            # print(current_time)

            # Model updates
            time_diff = current_time - self.previous_time
            if(time_diff.total_seconds() > PHYSICS_UPDATE_SECONDS):
                # q.put(self)
                # print(current_time)
                self.simulation.update(time_diff.total_seconds())
                # self.simulation.update(time_diff.total_seconds(), inputs)
                self.previous_time = current_time

            # Exiting
            # if simulation_is_ending:
            #     return

    def check_clients_input(self, q):
        """Check the Queue q for client input.

        Args:
            q (Queue): The queue with clients' inputs.

        Returns:
            list: The clients inputs in a list
        """
        inputs = []
        try:
            while not q.empty():
                inputs.append(q.get_nowait())
        except Queue.Empty:
            pass
        finally:
            return inputs

    def get_state(self):
        return self.simulation

    # def update_coisas(self, car_id, effectors):
    #
    #    self.simulation.update_car(car_id, effectors)

    # registar clientes
    # atualizar carro
    # a

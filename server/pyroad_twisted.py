# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

from twisted.internet import protocol, reactor, endpoints
from tools.helpers import ClientInput
import json


class Echo(protocol.Protocol):
    def __init__(self, factory, addr, q):
        self.factory = factory
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
            # c_in = ClientInput(self.addr, formatted_data)
            self.q.put(formatted_data)
            self.transport.write("Message received and parsed to JSON")
        except:
            self.transport.write("Invalid message")


class EchoFactory(protocol.Factory):
    def __init__(self, q):
        self.q = q

    def buildProtocol(self, addr):
        return Echo(self, addr, self.q)


def start(q):
    """Starts and runs the server connecting the Factory to the endpoint.

    It is a blocking run.
    """
    endpoints.serverFromString(reactor, "tcp:9001").listen(EchoFactory(q))
    reactor.run()

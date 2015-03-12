# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

from twisted.internet import protocol, reactor, endpoints
from tools.helpers import ClientInput


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
        self.transport.write(str(self.addr) + ": " + data)
        # print(dir(data))
        print(str(self.addr) + ": " + data)
        c_in = ClientInput(self.addr, data)
        self.q.put(c_in)


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

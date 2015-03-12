# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

from twisted.internet import protocol, reactor, endpoints
import threading
from tools.helpers import ClientInput


class Echo(protocol.Protocol):
    def __init__(self, q):
        self.q = q

    def dataReceived(self, data):
        self.transport.write(data)
        # print(dir(data))
        print(threading.current_thread().name)
        c_in = ClientInput("Nome", data)
        self.q.put(c_in)


class EchoFactory(protocol.Factory):
    def __init__(self, q):
        self.q = q

    def buildProtocol(self, addr):
        return Echo(self.q)


def start(q):
    endpoints.serverFromString(reactor, "tcp:9001").listen(EchoFactory(q))
    reactor.run()

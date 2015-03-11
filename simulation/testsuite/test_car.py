# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

# from mock import Mock
import mock
from mock import patch
import simulation.car
import unittest

class VehicleMock(object):
    """Singleton VehicleMocking used on several tests.

    Use to follow DRY principle.
    """

    vehicle = None

    @staticmethod
    def get_mocked_vehicle():
        from simulation.car import Car
        if VehicleMock.vehicle is None:
            VehicleMock.vehicle = Car("1", "")
            # VehicleMock.vehicle.name = "Coisa"
        return VehicleMock.vehicle

class CarTest(unittest.TestCase):

    def setUp(self):
        pass


    @patch('simulation.car.Car')
    def test_something(self, get_vehicle_mock):
        self.assertEqual("1", "1")

    @patch('simulation.car.Car')
    # @patch('invenio.modules.records.api.get_record')
    def test_record_mocking(self, get_vehicle_mock):
        """Tests the general mocking of Cars.
        """
        ## First get the mockeed record
        v = VehicleMock.get_mocked_vehicle()
        #print("Printing")
        #print(v)
        #print(dir(v))

        ## Assert general information
        self.assertEqual(v.name, 'Carr')

#TEST_SUITE = make_test_suite(CarTest)

#if __name__ == '__main__':
    #run_test_suite(TEST_SUITE)


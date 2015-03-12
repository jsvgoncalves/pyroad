# -*- coding: utf-8 -*-
#
## This file is part of PyRoad.
## 2014 João Gonçalves.

# from mock import Mock
# import mock
# from mock import patch
from simulation.car import Car
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

    def test_create_and_update(self):
        car_cfg = {}
        car_cfg['position'] = [1, 1]
        car_cfg['angle'] = 2
        car = Car("1", car_cfg)
        self.assertEqual(car.name, "1")
        self.assertEqual(car.position, [1, 1])
        self.assertEqual(car.angle, 2)

        car.update([2, 2], 1)  # [position], angle
        self.assertEqual(car.position, [2, 2])
        self.assertEqual(car.angle, 1)

    def test_car_with_routes(self):
        car_cfg = {}
        car_cfg['routes'] = {
            "route_size": 2,
            "route": [
                [1, 1, 0, 0],
                [2, 0, 0, 0]
            ]
        }
        car = Car("1", car_cfg)
        self.assertEqual(car.has_routes, True)

    def test_car_update_sensors(self):
        car_cfg = {}
        car_cfg['routes'] = {
            "route_size": 2,
            "route": [
                # t, s, a, b
                [1, 0, 1, 0],
                [2, 0, 0, 0]
            ]
        }
        car = Car("1", car_cfg)
        self.assertEqual(car.has_routes, True)
        sensor_data = {}
        sensor_data['elapsed_time'] = 1
        car.set_sensors(sensor_data)
        car.update([2, 2], 1)

        a, b, s = car.get_effectors()
        self.assertEqual(a, 1)
    # @patch('simulation.car.Car')
    # # @patch('invenio.modules.records.api.get_record')
    # def test_record_mocking(self, get_vehicle_mock):
    #     """Tests the general mocking of Cars.
    #     """
    #     # First get the mockeed record
    #     v = VehicleMock.get_mocked_vehicle()
    #     # print("Printing")
    #     # print(v)
    #     # print(dir(v))

    #     # Assert general information
    #     self.assertEqual(v.name, 'Carr')

# TEST_SUITE = make_test_suite(CarTest)

if __name__ == '__main__':
    unittest.main()
    # run_test_suite(TEST_SUITE)

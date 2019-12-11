import unittest

from parking_lot.src.ParkingManager import ParkingManager
from parking_lot.src.car_ticket import Car
from parking_lot.src.parkingboy import ParkingBoy
from parking_lot.src.parkinglot import ParkingLot


class TestParkingManager(unittest.TestCase):
    def test_should_car_can_be_parking_when_there_is_enough_space_in_any_packable_object(self):
        first_parking_lot = ParkingLot(1)
        second_parking_lot = ParkingLot(1)
        parking_boy = ParkingBoy([second_parking_lot])
        manager = ParkingManager([first_parking_lot, parking_boy])

        first_car = Car()
        second_car = Car()
        first_ticket = manager.park(first_car)
        second_ticket = manager.park(second_car)

        self.assertIsNotNone(first_ticket)
        self.assertIsNotNone(second_ticket)

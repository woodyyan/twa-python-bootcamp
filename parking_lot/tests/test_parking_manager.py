import unittest

from parking_lot.src.parking_manager import ParkingManager
from parking_lot.src.car_ticket import Car, Ticket
from parking_lot.src.exception import NoEnoughSpaceException
from parking_lot.src.parkingboy import ParkingBoy
from parking_lot.src.parkinglot import ParkingLot
from parking_lot.src.smart_parkingboy import SmartParkingBoy
from parking_lot.src.super_parkingboy import SuperParkingBoy


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

    def test_should_car_can_be_fetched_given_correct_ticket(self):
        parking_lot = ParkingLot(1)
        manager = ParkingManager([parking_lot])

        car = Car()
        ticket = manager.park(car)
        fetched_car = manager.fetch(ticket)

        self.assertEqual(fetched_car, car)

    def test_should_get_no_enough_space_exception_when_park_car_if_there_is_not_enough_position(self):
        parking_lot = ParkingLot(0)
        manager = ParkingManager([parking_lot])
        car = Car()

        self.assertRaises(NoEnoughSpaceException, manager.park, car)

    def test_should_get_none_with_ticket_which_is_not_exist(self):
        parking_lot = ParkingLot(1)
        manager = ParkingManager([parking_lot])
        car = manager.fetch(Ticket())

        self.assertIsNone(car)

    def test_should_all_parkable_object_can_be_managed_to_get_vehicle(self):
        parking_lot = ParkingLot(1)
        parking_boy = ParkingBoy([ParkingLot(1)])
        smart_parking_boy = SmartParkingBoy([ParkingLot(1)])
        super_parking_boy = SuperParkingBoy([ParkingLot(1)])
        manager = ParkingManager([parking_lot, parking_boy, smart_parking_boy, super_parking_boy])

        first_car = Car()
        second_car = Car()
        third_car = Car()
        forth_car = Car()
        first_ticket = manager.park(first_car)
        second_ticket = manager.park(second_car)
        third_ticket = manager.park(third_car)
        forth_ticket = manager.park(forth_car)

        self.assertEqual(manager.fetch(first_ticket), first_car)
        self.assertEqual(manager.fetch(second_ticket), second_car)
        self.assertEqual(manager.fetch(third_ticket), third_car)
        self.assertEqual(manager.fetch(forth_ticket), forth_car)

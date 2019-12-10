class NoEnoughSpaceException(Exception):
    pass


class ParkingLot:

    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__cars = {}

    def park(self, car):
        if self.__capacity <= len(self.__cars):
            raise NoEnoughSpaceException()
        ticket = Ticket()
        self.__cars[ticket] = car
        return ticket

    def fetch(self, ticket):
        if ticket in self.__cars:
            return self.__cars.pop(ticket)
        return None

    def is_full(self):
        return len(self.__cars) >= self.__capacity

    def contains_car(self, ticket):
        return ticket in self.__cars

    def get_available_space_count(self):
        return self.__capacity - len(self.__cars)

    def get_available_rate(self):
        return self.get_available_space_count() / self.__capacity


class Car:
    pass


class Ticket:
    pass

from ds.stack import Stack
from ds.queue import Queue
import sys


class Aircraft: 
    __slots__ = 'max_capacity', 'passenger_count', 'aircraft_storage', 'waiting_area'
    max_capacity: int
    passenger_count: int
    aircraft_storage: Stack
    waiting_area: Queue
    # waiting_area: SimpleQueue # For dev env

    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.aircraft_storage = Stack()
        self.passenger_count = 0
        self.waiting_area = Queue()
        # self.waiting_area = SimpleQueue() # For dev env

    def has_space(self):
        return self.passenger_count < self.max_capacity

    def is_full(self):
        return self.passenger_count == self.max_capacity

    def start_boarding(self, zones):
        print("Passengers are boarding the aircraft...")
        
        while (
            self.has_space() # While the aircraft has space
            and zones.has_passenger() # And there are people in zone queues
            ):
            # Allow one passenger 
            passenger = zones.next_passenger()
            # To board the plane
            self.board_passenger(passenger)
            # Increment passenger count
            self.passenger_count = self.passenger_count + 1
        return zones
        
    
    def board_passenger(self, passenger):
        print("\t ", end="")
        print(passenger)
        self.aircraft_storage.push(passenger)

    def take_off(self):
        if self.is_full():
            print("The aircraft is full.")

        print("Ready for taking off ...")
        print("The aircraft has landed.")

    def has_passenger(self):
        return self.passenger_count > 0

    def next_passenger(self):
        return self.aircraft_storage.pop()

    def disembark_passengers(self):
        print("Passengers are disembarking...")
        
        # For passengers with carry on
        buffer = Queue()
        # buffer = SimpleQueue() # For dev env

        # While there are passengers on the plane
        while self.has_passenger():
            
            # Ask one to disembark 
            passenger = self.aircraft_storage.pop()

            # Ask them to wait in waiting area if they have carry on
            if passenger.get_has_carry_on() == True: 
                buffer.enqueue(passenger)

            # Let them to deboard if they dont have carry on
            if passenger.get_has_carry_on() == False: 
                print("\t ", end='')
                print(passenger)
            
            # Decrement passenger count of aircraft
            self.passenger_count = self.passenger_count - 1

        # Let everyone in the waiting area deboard 
        while not buffer.is_empty():
            print("\t ", end='')
            print(buffer.dequeue())

        if not buffer.is_empty(): # For error checking
            print("Something is wrong, buffer is not empty")


from ds.stack import Stack
from ds.queue import Queue
import sys


class Aircraft: 
    """
    A class representing an aircraft for boarding and disembarking passengers.

    Attributes:
    - max_capacity (int): The maximum passenger capacity of the aircraft.
    - passenger_count (int): The current number of passengers on the aircraft.
    - aircraft_storage (Stack): A stack to store passengers on the aircraft.
    - waiting_area (Queue): A queue to store passengers waiting to board.

    Methods:
    - __init__(self, max_capacity): Initializes an aircraft with the specified maximum capacity.
    - has_space(self): Checks if there is space for more passengers on the aircraft.
    - is_full(self): Checks if the aircraft is at its maximum capacity.
    - start_boarding(self, zones): Initiates the boarding process by allowing passengers to board the aircraft.
    - board_passenger(self, passenger): Adds a passenger to the aircraft.
    - take_off(self): Prepares the aircraft for takeoff and informs about its status.
    - has_passenger(self): Checks if there are passengers on the aircraft.
    - next_passenger(self): Retrieves and removes the next passenger from the aircraft.
    - disembark_passengers(self): Initiates the disembarking process by letting passengers leave the aircraft and informs about their status.
    """

    __slots__ = 'max_capacity', 'passenger_count', 'aircraft_storage', 'waiting_area'
    max_capacity: int
    passenger_count: int
    aircraft_storage: Stack
    waiting_area: Queue
    # waiting_area: SimpleQueue # For dev env

    def __init__(self, max_capacity):
        """
        Initializes an aircraft with the specified maximum capacity.

        :param max_capacity: The maximum passenger capacity of the aircraft.
        """
        self.max_capacity = max_capacity
        self.aircraft_storage = Stack()
        self.passenger_count = 0
        self.waiting_area = Queue()
        # self.waiting_area = SimpleQueue() # For dev env

    def has_space(self):
        """
        Checks if there is space for more passengers on the aircraft.

        :return: True if there is space for more passengers, False otherwise.
        """
        return self.passenger_count < self.max_capacity

    def is_full(self):
        """
        Checks if the aircraft is at its maximum capacity.

        :return: True if the aircraft is full, False otherwise.
        """
        return self.passenger_count == self.max_capacity

    def start_boarding(self, zones):
        """
        Initiates the boarding process by allowing passengers to board the aircraft.

        :param zones: A collection of zones representing passenger queues.
        :return: The remaining passengers in the zones after boarding.
        """
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
        """
        Adds a passenger to the aircraft.

        :param passenger: The passenger to be added to the aircraft.
        """
        print("\t ", end="")
        print(passenger)
        self.aircraft_storage.push(passenger)

    def take_off(self):
        """
        Prepares the aircraft for takeoff and informs about its status.
        """
        if self.is_full():
            print("The aircraft is full.")

        print("Ready for taking off ...")
        print("The aircraft has landed.")

    def has_passenger(self):
        """
        Checks if there are passengers on the aircraft.

        :return: True if there are passengers on the aircraft, False otherwise.
        """
        return self.passenger_count > 0

    def next_passenger(self):
        """
        Retrieves and removes the next passenger from the aircraft.

        :return: The next passenger to disembark.
        """
        return self.aircraft_storage.pop()

    def disembark_passengers(self):
        """
        Initiates the disembarking process by letting passengers leave the aircraft and informs about their status.
        """
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

def main():
    return 

if __name__ == '__main__':
    main()

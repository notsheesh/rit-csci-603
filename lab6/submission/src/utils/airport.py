from ds.queue import Queue
from utils.passenger import Passenger

class Airport:
    """
    A class representing an airport for managing passengers' information.

    Attributes:
    - passenger_data (Queue): A queue for storing passenger data.
    - num_passengers (int): The number of passengers in the airport.

    Methods:
    - __init__(self): Initializes an airport with an empty passenger queue and zero passengers.
    - assemble_passengers(self, passenger_details): Adds passengers to the airport's passenger queue.
    - is_empty(self): Checks if the airport has no passengers.
    - has_passenger(self): Checks if the airport has passengers.
    - next_passenger(self): Retrieves and removes the next passenger from the airport's passenger queue.
    - __str__(self): Returns a string representation of the airport, listing passenger names.
    - get_num_passengers(self): Retrieves the number of passengers in the airport.
    """
    __slots__ = "passenger_data", "num_passengers"
    passenger_data: Queue
    num_passengers: int

    def __init__(self):
        """
        Initializes an airport with an empty passenger queue and zero passengers.
        """
        self.passenger_data = Queue()
        # self.passenger_data = SimpleQueue() # For dev env
        self.num_passengers = 0

    def assemble_passengers(self, passenger_details):
        """
        Adds passengers to the airport's passenger queue.

        :param passenger_details: A list of dictionaries containing passenger details.
        """
        for passenger in passenger_details:
            self.passenger_data.enqueue(
                Passenger(
                    passenger["name"], 
                    passenger["ticket_number"],
                    passenger["has_carry_on"]
                )
            )
            self.num_passengers += 1

    def is_empty(self):
        """
        Checks if the airport has no passengers.

        :return: True if there are no passengers in the airport, False otherwise.
        """
        return self.num_passengers == 0 

    def has_passenger(self):
        """
        Checks if the airport has passengers.

        :return: True if there are passengers in the airport, False otherwise.
        """
        return not self.num_passengers == 0 

    def next_passenger(self):
        """
        Retrieves and removes the next passenger from the airport's passenger queue.

        :return: The next passenger in the queue or None if the queue is empty.
        """
        if not self.is_empty(): 
            self.num_passengers -= 1
            return self.passenger_data.dequeue()
        else: 
            return None

    def __str__(self):
        """
        Returns a string representation of the airport, listing passenger names.

        :return: A string listing the names of passengers in the airport.
        """
        pretty_str = "Passengers:\n"
        for element in self.passenger_data.get_values():
            pretty_str += "{}\n".format(element.name)
        return pretty_str

    def get_num_passengers(self):
        """
        Retrieves the number of passengers in the airport.

        :return: The number of passengers in the airport.
        """
        return self.num_passengers

def main():
    pass

if __name__ == '__main__':
    main()
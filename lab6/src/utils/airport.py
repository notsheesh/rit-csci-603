from ds.queue import Queue
from utils.passenger import Passenger
class Airport:
    __slots__ = "passenger_data", "num_passengers"
    passenger_data: Queue
    num_passengers: int

    def __init__(self):
        self.passenger_data = Queue()
        # self.passenger_data = SimpleQueue() # For dev env
        self.num_passengers = 0

    def assemble_passengers(self, passenger_details):
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
        return self.num_passengers == 0 

    def has_passenger(self):
        return not self.num_passengers == 0 

    def next_passenger(self):
        if not self.is_empty(): 
            self.num_passengers -= 1
            return self.passenger_data.dequeue()
        else: 
            return None

    def __str__(self):
        pretty_str = "Passengers:\n"
        for element in self.passenger_data.get_values():
            pretty_str += "{}\n".format(element.name)
        return pretty_str

    def get_num_passengers(self):
        return self.num_passengers

def main():
    pass

if __name__ == '__main__':
    main()
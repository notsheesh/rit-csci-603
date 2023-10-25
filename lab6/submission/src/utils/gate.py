from ds.queue import Queue
from utils.zones import Zones

class Gate:
    """
    A class representing a gate for managing passengers' assembly and zones.

    Attributes:
    - max_capacity (int): The maximum capacity of the gate.
    - capacity (int): The current capacity of the gate.
    - storage (Queue): A queue for storing passengers waiting at the gate.

    Methods:
    - __init__(self, gate_max_capacity, capacity=0): Initializes a gate with the specified maximum capacity and optional current capacity.
    - has_space(self, zones): Checks if there is space for more passengers at the gate.
    - set_capacity(self, capacity): Sets the current capacity of the gate.
    - start_assembly(self, airport): Initiates the assembly process by allowing passengers to line up at the gate.
    """

    __slots__ = 'max_capacity', 'storage', 'capacity'
    max_capacity: int
    capacity: int
    storage: Queue 
    # storage: SimpleQueue # For dev env

    def __init__(self, gate_max_capacity, capacity = 0):
        """
        Initializes a gate with the specified maximum capacity and optional current capacity.

        :param gate_max_capacity: The maximum capacity of the gate.
        :param capacity: The current capacity of the gate.
        """
        self.max_capacity = gate_max_capacity
        self.capacity = capacity
        self.storage = Queue()
        # self.storage = SimpleQueue() # For dev env
    
    def has_space(self, zones):
        """
        Checks if there is space for more passengers at the gate.

        :param zones: The zones representing passenger queues.
        :return: True if there is space for more passengers at the gate, False otherwise.
        """
        return zones.get_num_total() < self.max_capacity

    def set_capacity(self, capacity):
        """
        Sets the current capacity of the gate.

        :param capacity: The current capacity of the gate.
        """
        self.capacity = capacity
    
    def start_assembly(self, airport):
        """
        Initiates the assembly process by allowing passengers to line up at the gate.

        :param airport: The airport containing passenger data.
        :return: The zones containing passengers and the updated airport.
        """
        print("Passengers are lining up at the gate...")
        
        zones = Zones()
        while (
            self.has_space(zones) # Gate/Zones haven't reached maximum capacity
            and airport.has_passenger() # 
        ):
            passenger = airport.next_passenger()
            zones.assemble_at_zone(passenger)
            print("\t ", end="")
            print(passenger)

        if not self.has_space(zones):
            print("The gate is full; remaining passengers must wait.")
            return zones, airport
        
        if airport.is_empty():
            print("The last passenger is in line!")
            return zones, airport
    
def main():
    pass

if __name__ == '__main__':
    main()
from ds.queue import Queue
from utils.zones import Zones

class Gate:
    __slots__ = 'max_capacity', 'storage', 'capacity'
    max_capacity: int
    capacity: int
    storage: Queue 
    # storage: SimpleQueue # For dev env

    def __init__(self, gate_max_capacity, capacity = 0):
        self.max_capacity = gate_max_capacity
        self.capacity = capacity
        self.storage = Queue()
        # self.storage = SimpleQueue() # For dev env
    
    def has_space(self, zones):
        return zones.get_num_total() < self.max_capacity

    def set_capacity(self, capacity):
        self.capacity = capacity
    
    def start_assembly(self, airport):
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
from ds.queue import Queue

class Zones: 
    """
    A class representing passenger zones for boarding an aircraft.

    Attributes:
    - zones_dict (dict): A dictionary of queues for each zone (A, B, C, D).
    - num_A (int): The number of passengers in Zone A.
    - num_B (int): The number of passengers in Zone B.
    - num_C (int): The number of passengers in Zone C.
    - num_D (int): The number of passengers in Zone D.
    - num_total (int): The total number of passengers across all zones.

    Methods:
    - __init__(self): Initializes the Zones object with empty queues for each zone and zero passenger counts.
    - has_passenger(self): Checks if there are passengers in any of the zones.
    - get_num_total(self): Returns the total number of passengers across all zones.
    - next_passenger(self): Returns the next passenger to board the aircraft, respecting zone priorities.
    - assemble_at_zone(self, passenger): Adds a passenger to the appropriate zone queue based on their zone letter.
    - debug(self): Prints the current state of each zone for debugging purposes.
    """
    __slots__ = "zones_dict", "num_A", "num_B", "num_C", "num_D", "num_total"
    zones_dict: dict
    num_A: int
    num_B: int
    num_C: int
    num_D: int
    num_total: int 


    def __init__(self):
        """
        Initializes the Zones object with empty queues for each zone and zero passenger counts.
        """
        self.zones_dict = {
            'A': Queue(),
            'B': Queue(),
            'C': Queue(),
            'D': Queue()
        }

        self.num_A = 0
        self.num_B = 0
        self.num_C = 0
        self.num_D = 0
        self.num_total = 0

    def has_passenger(self):
        """
        Checks if there are passengers in any of the zones.
        """
        return (
            self.num_D != 0 or
            self.num_C != 0 or
            self.num_B != 0 or
            self.num_A != 0
        )
    
    def get_num_total(self):
        """
        Returns the total number of passengers across all zones.
        """
        return self.num_total

    def next_passenger(self):
        """
        Returns the next passenger to board the aircraft, respecting zone priorities.
        """
        if self.num_D != 0:
            self.num_D -= 1
            self.num_total -= 1
            return self.zones_dict['D'].dequeue()
        
        if self.num_C != 0:
            self.num_C -= 1
            self.num_total -= 1
            return self.zones_dict['C'].dequeue()
        
        if self.num_B != 0:
            self.num_B -= 1
            self.num_total -= 1
            return self.zones_dict['B'].dequeue()
        
        if self.num_A != 0:
            self.num_A -= 1
            self.num_total -= 1
            return self.zones_dict['A'].dequeue()

    def assemble_at_zone(self, passenger):
        """
        Adds a passenger to the appropriate zone queue based on their zone letter.

        :param passenger: The passenger to be added to a zone.
        """
        passenger_zone = passenger.get_zone()
        # If ticket == Zone D
        if passenger_zone == "D":
            self.num_D += 1
            self.num_total += 1
            self.zones_dict["D"].enqueue(passenger)
            return
        # If ticket == Zone C
        if passenger_zone == "C":
            self.num_C += 1
            self.num_total += 1
            self.zones_dict["C"].enqueue(passenger)
            return
        # If ticket == Zone B
        if passenger_zone == "B":
            self.num_B += 1
            self.num_total += 1
            self.zones_dict["B"].enqueue(passenger)
            return
        # If ticket == Zone A
        if passenger_zone == "A":
            self.num_A += 1
            self.num_total += 1
            self.zones_dict["A"].enqueue(passenger)
            return

    def debug(self):
        """
        Prints the current state of each zone for debugging purposes.
        """
        if len(self.zones_dict.keys()) == 0:
            print("Zones dictionary empty")
        for key in self.zones_dict.keys():
            print("Zone {}: ".format(key), end='')
            print([x.get_ticket_number() for x in self.zones_dict[key].get_values()])
    

def main():
    return

if __name__ == '__main__':
    main()
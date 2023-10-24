from ds.queue import Queue

class Zones: 
    __slots__ = "zones_dict", "num_A", "num_B", "num_C", "num_D", "num_total"
    zones_dict: dict
    num_A: int
    num_B: int
    num_C: int
    num_D: int
    num_total: int 


    def __init__(self):
        self.zones_dict = {

            'A': Queue(),
            'B': Queue(),
            'C': Queue(),
            'D': Queue()

            # For dev env 
            # 'A': SimpleQueue(),
            # 'B': SimpleQueue(),
            # 'C': SimpleQueue(),
            # 'D': SimpleQueue(),

        }

        self.num_A = 0
        self.num_B = 0
        self.num_C = 0
        self.num_D = 0
        self.num_total = 0

    def has_passenger(self):
        return (
            self.num_D != 0 or
            self.num_C != 0 or
            self.num_B != 0 or
            self.num_A != 0
        )
    
    def get_num_total(self):
        return self.num_total

    def next_passenger(self):
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
        if len(self.zones_dict.keys()) == 0:
            print("Zones dictionary empty")
        for key in self.zones_dict.keys():
            print("Zone {}: ".format(key), end='')
            print([x.get_ticket_number() for x in self.zones_dict[key].get_values()])
    
from utils.airport import Airport
from utils.aircraft import Aircraft
from utils.gate import Gate
from utils.zones import Zones

class Simulation: 
    __slots__ = (
        'airport', 
        'aircraft', 
        'gate', 
        'zones'
    )

    aircraft: Aircraft
    gate: Gate
    zones: Zones
    airport: Airport

    def __init__(self, aircraft_max_capacity, gate_max_capacity):
        self.aircraft = Aircraft(aircraft_max_capacity)
        self.gate = Gate(gate_max_capacity)
        self.airport = None
        self.zones = None
    
    def run_simulation(self, airport):
        self.airport = airport

        print("Beginning simulation...")

        num_flights = 0
        num_people = self.airport.get_num_passengers()

        # While airport has passengers left 
        while self.airport.has_passenger():

            ( 
                self.zones, # Line up until gate has space, segregate in zones
                self.airport # Update waiting passengers in the airport
            ) = self.gate.start_assembly(self.airport)

            # While the zones have passengers
            while self.zones.has_passenger():   

                num_flights += 1

                # Board aircraft until its full
                self.zones = self.aircraft.start_boarding(self.zones)

                if not self.zones.has_passenger() and not self.aircraft.is_full():
                    print("There are no more passengers at the gate.")

                self.aircraft.take_off()
                self.aircraft.disembark_passengers() 
        
        print("Simulation complete. ", end="")
        print("Statistics: {} flights, {} passengers are at their destination".format(num_flights, num_people))
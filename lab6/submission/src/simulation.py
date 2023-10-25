from utils.airport import Airport
from utils.aircraft import Aircraft
from utils.gate import Gate
from utils.zones import Zones

class Simulation: 
    """
    A class representing a simulation of an airport boarding process.

    Attributes:
    - aircraft (Aircraft): An instance of the Aircraft class representing the aircraft used in the simulation.
    - gate (Gate): An instance of the Gate class representing the gate used in the simulation.
    - zones (Zones): An instance of the Zones class representing passenger segregation into zones.
    - airport (Airport): An instance of the Airport class containing passenger data.

    Methods:
    - __init__(self, aircraft_max_capacity, gate_max_capacity): Initializes a new Simulation instance with the specified aircraft and gate capacities.
    :param aircraft_max_capacity: The maximum capacity of the aircraft.
    :param gate_max_capacity: The maximum capacity of the gate.
    - run_simulation(self, airport): Runs the simulation of the airport boarding process using the specified airport.
    :param airport: The airport object containing passenger data.
    """
    
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
        """
        Initialize a new Simulation instance with the specified aircraft and gate 
        capacities.

        :param aircraft_max_capacity: The maximum capacity of the aircraft.
        :param gate_max_capacity: The maximum capacity of the gate.
        """
        self.aircraft = Aircraft(aircraft_max_capacity)
        self.gate = Gate(gate_max_capacity)
        self.airport = None
        self.zones = None
    
    def run_simulation(self, airport):
        """
        Run the simulation of the airport boarding process using the specified 
        airport.

        :param airport: The airport object containing passenger data.
        """
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

def main():
    return

if __name__ == '__main__':
    main()
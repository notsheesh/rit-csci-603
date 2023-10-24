from simulation import Simulation
from utils.helper import get_data, get_capacity
from utils.airport import Airport
from sys import argv as console_args

def main():
    """
    The main loop responsible for getting the input details from the user
    and running the AiRIT's simulation.
    :return: None
    """
    # Init aircraft and gate for simulation
    sim = Simulation(
        gate_max_capacity = get_capacity("Gate"), # stdin
        aircraft_max_capacity = get_capacity("Aircraft") # stdin
        )
    
    # # Gather passenger details
    passenger_data = get_data(console_args) 
    
    # # Let passengers into the airport  
    airport = Airport()
    airport.assemble_passengers(passenger_data)

    # # Debug - prints all passengers present at the airport
    # print(airport)

    # # Run simulation
    sim.run_simulation(airport = airport)

if __name__ == '__main__':
    main()
    
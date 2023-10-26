"""
AiRIT - Simulation

This script simulates the process of passengers boarding an aircraft at an airport and later disembarking. 
It provides a user interface to input parameters such as gate and aircraft capacities and reads passenger 
details from an external data file. The simulation demonstrates the orderly boarding and disembarkation 
of passengers in zones, replicating real-world airport operations.

The script consists of several components, including data structures for queues, a gate, and an airport, 
as well as a simulation class responsible for executing the simulation. It utilizes various utility functions 
to interact with the user and read passenger data.

To run the simulation, simply execute this script and provide the desired gate and aircraft capacities, 
as well as the passenger data file as a command-line argument.

Author: Shreesh Tripathi, st4083
"""
from simulation import Simulation
from utils.helper import get_data, get_capacity, parse_args
from utils.airport import Airport
from sys import argv as console_args

def main():
    """
    The main loop responsible for getting the input details from the user
    and running the AiRIT's simulation.
    :return: None
    """
    # Parse cmd line args 
    file_name = parse_args(console_args)

    # Init aircraft and gate for simulation
    sim = Simulation(
        gate_max_capacity = get_capacity("Gate"), # stdin
        aircraft_max_capacity = get_capacity("Aircraft") # stdin
        )
    
    # # Gather passenger details
    passenger_data = get_data(file_name) 
    
    # # Let passengers into the airport  
    airport = Airport()
    airport.assemble_passengers(passenger_data)

    # # Debug - prints all passengers present at the airport
    # print(airport)

    # # Run simulation
    sim.run_simulation(airport = airport)

if __name__ == '__main__':
    main()
    
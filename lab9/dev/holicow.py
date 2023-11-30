"""
CSCI 603 Lab 09: Holi Cow!

This script runs a simulation of a paintball game on a field populated with cows. 
It utilizes the classes defined in the 'simulation' module, including the Simulation class, 
which orchestrates the entire simulation. The simulation involves paintballs splashing on cows 
based on their proximity, and the script displays the results of the simulation, highlighting the 
best choice of paintball and the painted cows.

Usage:
    python3 holicow.py {filename}

    - {filename}: The name of the file containing information about cows and paintballs in the field.

Make sure to provide the filename as a command-line argument when running the script.

Author: Shreesh Tripathi, st4083 
"""

from simulation import Simulation

def main():
    """
    Main function to run the Holi Cow simulation.

    Sets up the simulation, displays the field of dreams, runs the simulation, and displays the results.
    """
    # setup
    sim = Simulation()
    sim.setup()
    
    # pretty 
    print("Field of Dreams")
    print(sim.field)

    # simulate
    print("\nBeginning simulation...")
    sim.simulate()

    # result
    print("\nResults:")
    sim.display_result()
    
if __name__ == "__main__":
    main()
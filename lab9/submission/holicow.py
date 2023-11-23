"""
CSCI 603 Lab 09: Holi Cow!

This script defines a simulation of paintball interactions between cows in a field. It includes a Simulation class
that reads input data, sets up the initial state, simulates paintball paths to cows, and analyzes the results to
determine the best outcome. The simulation is based on a graph representation of the field and incorporates
classes such as Graph, Vertex, Paintball, and Cow.

Author: Shreesh Tripathi, st4083 
"""

from simulation import Simulation

def main():
    Simulation().run()

if __name__ == "__main__":
    main()
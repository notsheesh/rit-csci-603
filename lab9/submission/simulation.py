from graph import Graph
from vertex import Vertex
from paintball import Paintball
from cow import Cow
import sys

class Simulation:
    """
    A class representing a simulation of paintball splashes on cows in a field.

    Attributes:
        cows (list): List of Cow objects representing the cows in the field.
        balls (list): List of Paintball objects representing the paintballs in the field.
        field (Graph): A Graph object representing the field with cows and paintballs as vertices.
        result (dict): A dictionary containing simulation results, including the best paintball choice.

    Methods:
        setup(): Sets up the simulation by reading data from a file, creating cows and paintballs, and initializing the field.
        read_file(filename: str) -> Tuple[list, list]: Reads data from a file and returns lists of cows and paintballs.
        setup_field() -> Graph: Initializes the field graph by adding edges between paintballs and cows within splash range.
        reset_session(): Resets the trigger session by marking all vertices as not triggered.
        trigger(ball_vtx: Vertex, new_session: bool = False, count: int = None, cp_map: dict = None) -> Tuple[int, dict]:
            Triggers a paintball and simulates the splash effect on cows and other paintballs in the field.
        simulate(): Runs the simulation for each paintball and determines the best choice based on the most painted cows.
        display_result(): Displays the simulation results, including the best paintball choice and painted cows.
    """
    def __init__(self):
        """
        Initializes a new Simulation instance with attributes for cows, paintballs, field, and results.
        """
        self.cows = None
        self.balls = None
        self.field = None
        self.result = {
            "color": None,
            "count": -999,
            "cp_map": {}
        }
        
    def setup(self):
        """
        Sets up the simulation by parsing command-line arguments, reading data from a file, and initializing the field.
        Exits the program if the filename is not provided or the file is not found.
        """
        if len(sys.argv) != 2:
            print("Usage: python3 holicow.py {filename}")
            sys.exit(1)
        
        filename = sys.argv[1]
        self.cows, self.balls = self.read_file(filename)
        self.field = self.setup_field() 

        # print(len(self.cows), len(self.balls))

        if len(self.cows) == 0 and len(self.balls) == 0: # tc5
            print("No paintballs or cows found on the field")
            sys.exit(1)

        if len(self.balls) == 0: # tc6
            print("No paintballs found on the field")
            sys.exit(1)
        
        if len(self.cows) == 0: # tc7
            print("[ALERT] No cows were found on the field.")
            yn = input("Do you still wish to simulate? (y/n): ")
            if yn == "n":
                return False
            print("----------------------------------------------------")
        
        return True

    

    def read_file(self, filename):
        """
        Reads data from a file and returns lists of cows and paintballs.

        :param filename: The name of the file containing cow and paintball data.
        :type filename: str

        :return: Lists of Cow and Paintball objects.
        :rtype: Tuple[list, list]
        """
        try: 
            with open(filename, 'r') as file:
                cows = []
                balls = []
                for line in file:
                    data = line.strip().split()
                    if data[0] == 'cow':
                        name = data[1]
                        loc = (float(data[2]), float(data[3]))
                        cows.append(Cow(name, loc))

                    elif data[0] == 'paintball':
                        name = data[1]
                        loc = (float(data[2]), float(data[3]))
                        rad = float(data[4])
                        balls.append(Paintball(name, loc, rad))

                return cows, balls

        except FileNotFoundError as e:
            print(f"File not found: {filename}")
            sys.exit(1)

    def setup_field(self):
        """
        Initializes the field graph by adding edges between paintballs and cows within splash range.

        :return: The Graph object representing the field.
        :rtype: Graph
        """
        field = Graph()
        for ball in self.balls:
            floating = True
            # add cows in range
            for cow in self.cows:
                if ball.will_splash(cow):
                    field.add_edge(ball, cow, ball.eu_dist(cow))

            # add balls in range
            for otherBall in self.balls: 
                if ball != otherBall and ball.will_splash(otherBall):
                    field.add_edge(ball, otherBall, ball.eu_dist(otherBall))
        
        # add floating nodes
        for node in self.balls + self.cows:
            if node.id not in field:
                field.add_vertex(node)

        return field

    def reset_session(self):
        """
        Resets the trigger session by marking all vertices as not triggered.
        """
        for vertex in self.field:
            vertex.triggered = False

    def trigger(self, ball_vtx, new_session = False, count = None, cp_map = None):
        """
        Triggers a paintball and simulates the splash effect on cows and other paintballs in the field.

        :param ball_vtx: The Vertex corresponding to the paintball to be triggered.
        :type ball_vtx: Vertex
        :param new_session: Indicates whether a new trigger session is starting.
        :type new_session: bool
        :param count: The current count of painted cows.
        :type count: int
        :param cp_map: A mapping of cows to the paintballs that painted them.
        :type cp_map: dict

        :return: Tuple containing the updated count and cp_map.
        :rtype: Tuple[int, dict]
        """
        if new_session:
            print(f"Triggering {ball_vtx.id} paintball...")
            ball_vtx.triggered = True
            count = 0
            cp_map = {}
        
        # splash all vertices in range of the paintball
        for nbr_vtx in ball_vtx.get_neighbors(): 
            # if cow, paint it
            if nbr_vtx.type == "cow":
                count += 1
                nbr_vtx.painted_by.append(ball_vtx)
                print(f"\t{nbr_vtx.id} is painted {ball_vtx.id}!")

                # log paint -> cow event for a ball_vtx (origin) trigger
                if nbr_vtx.id in cp_map:
                    cp_map[nbr_vtx.id].append(ball_vtx)
                else: 
                    cp_map[nbr_vtx.id] = [ball_vtx]

            # if paintball, trigger it
            elif nbr_vtx.type == "ball":
                if nbr_vtx.triggered:
                    # print(f"\t[LOG]: {nbr_vtx.id} already triggered.")
                    pass
                else:
                    print(f"\t{nbr_vtx.id} paintball is triggered by {ball_vtx.id} paint ball")
                    nbr_vtx.triggered = True
                    count, cp_map = self.trigger(ball_vtx=nbr_vtx, count=count, cp_map=cp_map)

        return count, cp_map

    def simulate(self):
        """
        Runs the simulation for each paintball and determines the best choice based on the most painted cows.
        """
        for ball in self.balls:
            ball_vtx: Vertex = self.field.get_vertex(ball.id)
            self.reset_session()
            count, cp_map = self.trigger(ball_vtx, new_session=True)
            if count > self.result['count']:
                self.result['color'] = ball_vtx
                self.result['count'] = count
                self.result['cp_map'] = cp_map

    def display_result(self):
        """
        Displays the simulation results, including the best paintball choice and painted cows.
        """
        if self.result['count'] == 0:
            print("No cows were painted by any starting paint ball!")
            return
        
        print(f"Triggering the {self.result['color'].id} paintball is the best choice with {self.result['count']} total paint on the cows:")
        for cow in self.result['cp_map']:
            paints = ''
            for paint in self.result['cp_map'][cow]:
                paints += f"'{paint.id}', "
            paints = "{" + paints[:-2] + "}"
            print(f"\t{cow}’s colors: {paints}")
        
        # house keeping
        for vertex in self.field:
            if vertex.type == "cow" and vertex.id not in self.result['cp_map']:
                paints = "{}"
                print(f"\t{vertex.id}’s colors: {paints}")
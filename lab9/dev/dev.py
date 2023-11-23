from graph import Graph
from vertex import Vertex
from paintball import Paintball
from cow import Cow
import sys


class Simulation():
    def __init__(self):
        self.balls = []
        self.cows = []
        self.field = None

    def read_file(self, filename):
        try: 
            with open(filename, 'r') as file:
                for line in file:
                    data = line.strip().split()
                    if data[0] == 'cow':
                        name = data[1]
                        loc = (int(data[2]), int(data[3]))
                        self.cows.append(Cow(name, loc))

                    elif data[0] == 'paintball':
                        name = data[1]
                        loc = (int(data[2]), int(data[3]))
                        rad = int(data[4])
                        self.balls.append(Paintball(name, loc, rad))

        except FileNotFoundError as e:
            print(f"File not found: {filename}")
            sys.exit(1)

    def init_cow_map(self):
        cow_map = {}
        for cow in self.cows:
            cow_map[cow.id] = set()
        return cow_map
    
    def trigger(self,ball, paths, result, graph, cow_map, count = 0, triggered = set(), paints = set()):
        while paths:
            path = paths.pop(0).copy() 
            while path:
                vtx = path.pop(0)
                if graph.get_type(vtx) == "cow":
                    if graph.get_vertex(ball).will_splash(graph.get_vertex(vtx)):
                        count += 1
                        cow_map[vtx].add(ball)
                        print(f"\t{vtx} was painted {ball}!")
                elif graph.get_type(vtx) == "ball" and (vtx, ball) not in triggered:
                    count += 1
                    print(f"\t{vtx} paintball is triggered by {ball} paint ball")
                    triggered.add((vtx, ball))
                    paints.add(vtx)
                    self.trigger(vtx, result[vtx].copy(), result, graph, cow_map, count, triggered, paints) 
        return count, cow_map, triggered, paints
    
    def rerun(self, result, cow_map, graph = None):
        if graph is None:
            graph = self.field
        max_count, max_ball, max_cow_map, paints = -1, '', None, None
        for ball in result:
            triggered = set()
            print(f"Triggering {ball} paintball...")
            count, cow_map, triggered, _paints = self.trigger(ball, result[ball].copy(), result, graph, cow_map) 
            if count > max_count:
                max_count, max_ball, max_cow_map = count, ball, cow_map
                paints = _paints
                paints.add(ball)
        return max_count, max_ball, cow_map, paints
    
    def preprocess(self, paths):
        result = {}
        color = ''
        for (ball, cow), path in paths.items():
            result[ball] = result.get(ball, []) + [path[1:]]
        return result
        
    def simulate(self):
        paths = {}
        for ball in self.balls:
            for cow in self.cows:
                ballVx = self.field.get_vertex(ball.id)
                cowVx = self.field.get_vertex(cow.id)
                path = self.field.find_paths(ballVx, cowVx)
                if path is not None:
                    paths[(ballVx.id, cowVx.id)] = [vtx.id for vtx in path]
        return self.preprocess(paths)
    
    def setup_sim(self):
        if len(sys.argv) != 2:
            print("Usage: python3 holicow.py {filename}")
            sys.exit(1)

        self.read_file(sys.argv[1])
        self.field = Graph()
        for ball in self.balls:
            for cow in self.cows:
                if ball.will_splash(cow):
                    self.field.add_edge(ball, cow, ball.eu_dist(cow))

            for otherBall in self.balls: 
                if ball != otherBall and ball.will_splash(otherBall):
                    self.field.add_edge(ball, otherBall, ball.eu_dist(otherBall))

    def count_paints(self, max_cow_map, paints_triggered):
        paints = []
        for cow in max_cow_map:
            for paint in max_cow_map[cow]:
                if paint in paints_triggered:
                    paints.append(paint)
        return len(paints)

    def get_best_outcome(self, max_cow_map, paints_triggered):
        for cow in max_cow_map:
            color_str = ''
            for color in max_cow_map[cow]:
                if color in paints_triggered:
                    color_str += "'" + color + "'" + ", "
            if len(color_str) != 0:
                color_str = color_str[:-2]
            color_str = "{" + color_str + "}"
            print(f"\t{cow}'s colors: {color_str}")

    def run(self):
        self.setup_sim()

        print("Field of Dreams")
        print(self.field)

        print("\nBeginning simulation...")
        results = self.simulate()
        max_count, max_ball, max_cow_map, paints_triggered = self.rerun(results, self.init_cow_map())
        count = self.count_paints(max_cow_map, paints_triggered)
        
        print("\nResults:")
        print(f"Triggering the {max_ball} paintball is the best choice with {count} total paint on the cows:")
        self.get_best_outcome(max_cow_map, paints_triggered)

def main():
    Simulation().run()

if __name__ == "__main__":
    main()
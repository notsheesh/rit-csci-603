from graph import Graph
from vertex import Vertex
from paintball import Paintball
from cow import Cow

cows = []

def read_file(filename):
    balls = []

    try: 
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split()
                if data[0] == 'cow':
                    name = data[1]
                    loc = (int(data[2]), int(data[3]))
                    cows.append(Cow(name, loc))

                elif data[0] == 'paintball':
                    name = data[1]
                    loc = (int(data[2]), int(data[3]))
                    rad = int(data[4])
                    balls.append(Paintball(name, loc, rad))

    except FileExistsError as e:
        print(f"File not found: {e}")
    
    return cows, balls

def find_paths(start, end):
    visited = set()
    visited.add(start.id)
    return dfs(start, end, visited)

def dfs(current, goal, visited):
    if current.id == goal.id:
        return [goal]
    
    for neighbor in current.get_neighbors():
        if neighbor.id not in visited:
            visited.add(neighbor.id)
            path = dfs(neighbor, goal, visited)

            if path != None:
                path.insert(0, current)
                return path
    return None

def init_cow_map():
    cow_map = {}
    for cow in cows:
        cow_map[cow.id] = set()
    return cow_map

def trigger(ball, paths, result, graph, cow_map, count = 0, triggered = set()):
    while paths:
        path = paths.pop(0).copy() 
        while path:
            vtx = path.pop(0)
            if graph.get_type(vtx) == "cow":
                if (
                    graph.get_vertex(ball).will_splash(graph.get_vertex(vtx)) and
                        (vtx, ball) not in triggered):
                    count += 1
                    cow_map[vtx].add(ball)
                    print(f"\t{vtx} was painted {ball}!")
                    triggered.add((vtx, ball))
            elif graph.get_type(vtx) == "ball" and (vtx, ball) not in triggered:
                count += 1
                print(f"\t{vtx} paintball is triggered by {ball} paint ball")
                triggered.add((vtx, ball))
                trigger(vtx, result[vtx].copy(), result, graph, cow_map, count, triggered) 
    return count, cow_map, triggered
        
def rerun(result, graph, cow_map):
    max_count = -1 
    max_ball = ''
    max_cow_map = None
    paints_triggered = None
    for ball in result:
        triggered = set()
        print(f"Triggering {ball} paintball...")
        count, cow_map, triggered = trigger(ball, result[ball].copy(), result, graph, cow_map) 
        if count > max_count:
            max_count = count
            max_ball = ball
            max_cow_map = cow_map
            paints_triggered = triggered
            paints_triggered.add(ball)
    return max_count, max_ball, cow_map, paints_triggered

def preprocess(paths):
    result = {}
    color = ''
    for (ball, cow), path in paths.items():
        result[ball] = result.get(ball, []) + [path[1:]]
    return result
        
def simulate(field, balls, cows):
    paths = {}
    for ball in balls:
        for cow in cows:
            ballVx = field.get_vertex(ball.id)
            cowVx = field.get_vertex(cow.id)
            path = find_paths(ballVx, cowVx)
            if path is not None:
                paths[(ballVx.id, cowVx.id)] = [vtx.id for vtx in path]
    return preprocess(paths)
    
def main():
    cows, balls = read_file('data.txt')
    # print([str(cow) for cow in cows])
    # print([str(ball) for ball in balls])
    
    field = Graph()
    for ball in balls:
        for cow in cows:
            if ball.will_splash(cow):
                field.add_edge(ball, cow, ball.eu_dist(cow))

        for otherBall in balls: 
            if ball != otherBall and ball.will_splash(otherBall):
                field.add_edge(ball, otherBall, ball.eu_dist(otherBall))

    print(field)

    print("\nBeginning simulation...")


    results = simulate(field, balls, cows)

    # path = find_paths(field.get_vertex('RED'), field.get_vertex('Babe'))
    # print([vtx.id for vtx in path])

    cow_map = init_cow_map()

    max_count, max_ball, max_cow_map, paints_triggered = rerun(results, field, cow_map)

    paints = []
    for cow in max_cow_map:
        for paint in max_cow_map[cow]:
            paints.append(paint)

    print("Results:")
    print(f"Triggering the {max_ball} paintball is the best choice with {len(paints)} total paint on the cows:")
    for cow in max_cow_map:
        color_str = ''
        # for color in max_cow_map[cow]:
        #     if color in paints_triggered:
        #         color_str += color + ", "
        # color_str = ''.join(list(color_str).pop())
        print(f"\t{cow}'s colors: {color_str}")
    
    print(paints_triggered)

if __name__ == "__main__":
    main()
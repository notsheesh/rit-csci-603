class Paintball:
    def __init__(self, id, loc, r):
        self.id = id
        self.loc = loc
        self.r = r
        self.type = "ball"

    def eu_dist(self, point):
        x1, y1 = self.loc
        x2, y2 = point.loc
        return  ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    def will_splash(self, point):
        return self.eu_dist(point) <= self.r

    def __str__(self):
        return self.id
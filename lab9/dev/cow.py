class Cow:
    def __init__(self, id, loc):
        self.id = id
        self.loc = loc
        self.r = 0
        self.type = "cow"

    def __str__(self):
        return self.id

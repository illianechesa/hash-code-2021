class Intersection:
    def __init__(self, id):
        self.id = id
        self.incoming_streets = []

    def add_street(self, street):
        self.incoming_streets.append(street)

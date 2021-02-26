class Street:
    def __init__(self, text):
        self.start_intersection, self.end_intersection, self.name, self.time = text.split(
            ' ')


class Intersection:
    def __init__(self, id):
        self.id = id
        self.incoming_streets = []

    def add_street(self, street):
        self.incoming_streets.append(street)


class Car:
    def __init__(self, text):
        self.nbr_streets, *self.text_streets = text.split(' ')

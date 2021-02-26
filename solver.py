from collections import Counter
from models import Street, Intersection, Car

def solve(data, filename):

    duration, intersections_number, streets_number, cars_number, score = data.pop(
        0).split(' ')

    streets = []
    intersections = {}
    paths = []

    for i in range(0, int(streets_number)):
        line = data.pop(0)

        if not line.split(' ')[1] in intersections.keys():
            intersections[line.split(' ')[1]] = Intersection(
                line.split(' ')[1])
            intersections[line.split(' ')[1]].add_street(line.split(' ')[2])
        else:
            intersections[line.split(' ')[1]].add_street(line.split(' ')[2])
        streets.append(Street(line))

    for i in range(0, int(cars_number)):
        paths.append(Car(data.pop(0)))

    return intersections
      



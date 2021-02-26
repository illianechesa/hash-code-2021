from collections import Counter
from models import Street, Intersection, Car


def solve(data, filename):

    duration, intersections_number, streets_number, cars_number, score = data.pop(
        0).split(' ')

    intersections = {}
 
    for i in range(0, int(streets_number)):
        line = data.pop(0)
        end_street = line.split(' ')[1]
        street_name = line.split(' ')[2]

        if not end_street in intersections.keys():
            intersections[end_street] = Intersection(end_street)
            intersections[end_street].add_street(street_name)
        else:
            intersections[end_street].add_street(street_name)

    return intersections

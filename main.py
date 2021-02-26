# Import all libraries
import sys

input_file = sys.argv[1]

# Import local libraries
from input import parse_input
from solver import solve
from output import save


if __name__ == "__main__":
  data = parse_input(filename=input_file)
  intersections = solve(data, input_file)
  save(input_file, intersections)
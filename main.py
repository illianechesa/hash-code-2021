# Import all libraries
import sys

input_file = sys.argv[1]

# Import local libraries
from input import parse_input
from solver import solve


if __name__ == "__main__":
  data = parse_input(filename=input_file)
  solve(data, input_file)
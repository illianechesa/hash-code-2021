def parse_input(filename):

    with open(f"./inputs/{filename}", 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
    f.close()
    return lines

def save(filename, intersections):
  with open(f"./results/{filename.split('.')[0]}_output.txt", 'w') as f:

    f.write(str(len(intersections.keys())) + "\n")
    for k, v in intersections.items():
        f.write(v.id + "\n")
        f.write(str(len(v.incoming_streets)) + "\n")
        for street in v.incoming_streets:
            f.write(street + " 1" + "\n")

    f.close()
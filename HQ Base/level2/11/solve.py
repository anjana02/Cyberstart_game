with open("latin.txt", "r") as f:

    lines = f.read()

    slines = lines.split(".")
    for row in slines:
        print(row)

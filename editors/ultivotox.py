def ultivotox_1_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("ultiovotox1.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def ultivotox_2_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("ultiovotox2.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def ultivotox_3_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("ultiovotox3.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def ultivotox_4_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("ultiovotox4.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def ultivotox_5_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("ultiovotox5.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def ultivotox_6_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("ultiovotox6.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def ultivotox_7_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("ultiovotox7.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def ultivotox_8_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("ultiovotox8.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def ultivotox_9_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("ultiovotox9.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def ultivotox_10_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("ultiovotox10.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)
    
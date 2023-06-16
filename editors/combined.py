def combined_1_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("combined1.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_2_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("combined2.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_3_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("combined3.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_4_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("combined4.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_5_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("combined5.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_6_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("combined6.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_7_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("combined7.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_8_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("combined8.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_9_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("combined9.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_10_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("combined10.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][2:5] == "C2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][2:5] == "E2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][2:5] == "G1":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)

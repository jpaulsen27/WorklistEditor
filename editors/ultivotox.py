def ultivotox_1_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("ultiovotox1.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG8,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG8,,", file=output)
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
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[0] == "CAL0003POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG8,,", file=output)
        if line[0] == "CAL0004POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG8,,", file=output)
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
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[0] == "CAL0005POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG8,,", file=output)
        if line[0] == "CAL0006POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG8,,", file=output)
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
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[0] == "CAL0007POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG8,,", file=output)
        if line[0] == "CAL0008POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG8,,", file=output)
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
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[0] == "CAL0009POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG8,,", file=output)
        if line[0] == "CAL00010POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG8,,", file=output)
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
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[0] == "CAL0011POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG8,,", file=output)
        if line[0] == "CAL0012POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG8,,", file=output)
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
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[0] == "CAL0013POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG8,,", file=output)
        if line[0] == "CAL0014POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG8,,", file=output)
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
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[0] == "CAL0015POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG8,,", file=output)
        if line[0] == "CAL0016POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG8,,", file=output)
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
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[0] == "CAL0017POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG8,,", file=output)
        if line[0] == "CAL0018POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG8,,", file=output)
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
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG7,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[0] == "CAL0019POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG8,,", file=output)
        if line[0] == "CAL0020POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG8,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)
    
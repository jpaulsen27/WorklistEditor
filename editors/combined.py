def combined_1_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("combined1.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG7,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,COMBINED.m,NEG8,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P2E1,COMBINED.m,NEG8,,", file=output)
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
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG7,,", file=output)
        if line[0] == "CAL0003POST":
            print("NEG,P1E1,COMBINED.m,NEG8,,", file=output)
        if line[0] == "CAL0004POST":
            print("NEG,P2E1,COMBINED.m,NEG8,,", file=output)
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
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG7,,", file=output)
        if line[0] == "CAL0005POST":
            print("NEG,P1E1,COMBINED.m,NEG8,,", file=output)
        if line[0] == "CAL0006POST":
            print("NEG,P2E1,COMBINED.m,NEG8,,", file=output)
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
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG7,,", file=output)
        if line[0] == "CAL0007POST":
            print("NEG,P1E1,COMBINED.m,NEG8,,", file=output)
        if line[0] == "CAL0008POST":
            print("NEG,P2E1,COMBINED.m,NEG8,,", file=output)
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
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG7,,", file=output)
        if line[0] == "CAL0009POST":
            print("NEG,P1E1,COMBINED.m,NEG8,,", file=output)
        if line[0] == "CAL0010POST":
            print("NEG,P2E1,COMBINED.m,NEG8,,", file=output)
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
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG7,,", file=output)
        if line[0] == "CAL0011POST":
            print("NEG,P1E1,COMBINED.m,NEG8,,", file=output)
        if line[0] == "CAL0012POST":
            print("NEG,P2E1,COMBINED.m,NEG8,,", file=output)
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
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG7,,", file=output)
        if line[0] == "CAL0013POST":
            print("NEG,P1E1,COMBINED.m,NEG8,,", file=output)
        if line[0] == "CAL0014POST":
            print("NEG,P2E1,COMBINED.m,NEG8,,", file=output)
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
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG7,,", file=output)
        if line[0] == "CAL0015POST":
            print("NEG,P1E1,COMBINED.m,NEG8,,", file=output)
        if line[0] == "CAL0016POST":
            print("NEG,P2E1,COMBINED.m,NEG8,,", file=output)
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
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG7,,", file=output)
        if line[0] == "CAL0017POST":
            print("NEG,P1E1,COMBINED.m,NEG8,,", file=output)
        if line[0] == "CAL0018POST":
            print("NEG,P2E1,COMBINED.m,NEG8,,", file=output)
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
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG7,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG2,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG4,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG6,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG1,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG3,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG5,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG7,,", file=output)
        if line[0] == "CAL0019POST":
            print("NEG,P1E1,COMBINED.m,NEG8,,", file=output)
        if line[0] == "CAL0020POST":
            print("NEG,P2E1,COMBINED.m,NEG8,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)

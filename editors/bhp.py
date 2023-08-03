def bhp_1_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("bhp1.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_2_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("bhp2.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_3_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("bhp3.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_4_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("bhp4.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_5_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("bhp5.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_6_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("bhp6.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_7_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("bhp7.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_8_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("bhp8.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_9_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("bhp9.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_10_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("bhp10.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)

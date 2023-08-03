def etoh_1_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("etoh1.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,ETOH.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,ETOH.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,ETOH.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,ETOH.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[5] == "L1":
            line[1] = "VIAL 2"
        if line[5] == "QC1":
            line[1] = "VIAL 3"
        if line[5] == "QC2":
            line[1] = "VIAL 4"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", file=output)


def etoh_2_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("etoh2.csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[5] == "L1":
            line[1] = "VIAL 2"
        if line[5] == "QC1":
            line[1] = "VIAL 3"
        if line[5] == "QC2":
            line[1] = "VIAL 4"
        if line[1][1] == "1":
            line[1] = "P3" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P4" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def etoh_3_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("etoh3.csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[5] == "L1":
            line[1] = "VIAL 2"
        if line[5] == "QC1":
            line[1] = "VIAL 3"
        if line[5] == "QC2":
            line[1] = "VIAL 4"
        if line[1][1] == "1":
            line[1] = "P5" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P6" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def etoh_4_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("etoh4.csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[5] == "L1":
            line[1] = "VIAL 2"
        if line[5] == "QC1":
            line[1] = "VIAL 3"
        if line[5] == "QC2":
            line[1] = "VIAL 4"
        if line[1][1] == "1":
            line[1] = "P7" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P8" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def etoh_5_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("etoh5.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,ETOH.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,ETOH.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,ETOH.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,ETOH.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[5] == "L1":
            line[1] = "VIAL 2"
        if line[5] == "QC1":
            line[1] = "VIAL 3"
        if line[5] == "QC2":
            line[1] = "VIAL 4"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", file=output)


def etoh_6_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("etoh6.csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[5] == "L1":
            line[1] = "VIAL 2"
        if line[5] == "QC1":
            line[1] = "VIAL 3"
        if line[5] == "QC2":
            line[1] = "VIAL 4"
        if line[1][1] == "1":
            line[1] = "P3" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P4" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def etoh_7_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("etoh7.csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[5] == "L1":
            line[1] = "VIAL 2"
        if line[5] == "QC1":
            line[1] = "VIAL 3"
        if line[5] == "QC2":
            line[1] = "VIAL 4"
        if line[1][1] == "1":
            line[1] = "P5" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P6" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def etoh_8_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("etoh8.csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[5] == "L1":
            line[1] = "VIAL 2"
        if line[5] == "QC1":
            line[1] = "VIAL 3"
        if line[5] == "QC2":
            line[1] = "VIAL 4"
        if line[1][1] == "1":
            line[1] = "P7" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P8" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def etoh_9_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("etoh9.csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[5] == "L1":
            line[1] = "VIAL 2"
        if line[5] == "QC1":
            line[1] = "VIAL 3"
        if line[5] == "QC2":
            line[1] = "VIAL 4"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def etoh_10_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("etoh10.csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[5] == "L1":
            line[1] = "VIAL 2"
        if line[5] == "QC1":
            line[1] = "VIAL 3"
        if line[5] == "QC2":
            line[1] = "VIAL 4"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)

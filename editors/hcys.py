def hcys_1_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("hcys1.csv", 'w')
    print(lines[0], end="", file=output)
    print("Blank1,VIAL 1,HCYS.m,Blank1,,", file=output)
    print("Blank2,VIAL 1,HCYS.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,HCYS.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,HCYS.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,HCYS.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "Functional Biomarker.m":
            line[2] = "HCYS.m"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def hcys_2_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("hcys2.csv", 'w')
    print(lines[0], end="", file=output)
    print("Blank1,VIAL 1,HCYS.m,Blank1,,", file=output)
    print("Blank2,VIAL 1,HCYS.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,HCYS.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,HCYS.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,HCYS.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "Functional Biomarker.m":
            line[2] = "HCYS.m"
        if line[1][1] == "1":
            line[1] = "P3" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P4" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_3_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("hcys3.csv", 'w')
    print(lines[0], end="", file=output)
    print("Blank1,VIAL 1,HCYS.m,Blank1,,", file=output)
    print("Blank2,VIAL 1,HCYS.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,HCYS.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,HCYS.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,HCYS.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "Functional Biomarker.m":
            line[2] = "HCYS.m"
        if line[1][1] == "1":
            line[1] = "P5" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P6" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_4_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("hcys4.csv", 'w')
    print(lines[0], end="", file=output)
    print("Blank1,VIAL 1,HCYS.m,Blank1,,", file=output)
    print("Blank2,VIAL 1,HCYS.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,HCYS.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,HCYS.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,HCYS.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "Functional Biomarker.m":
            line[2] = "HCYS.m"
        if line[1][1] == "1":
            line[1] = "P7" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P8" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_5_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("hcys5.csv", 'w')
    print(lines[0], end="", file=output)
    print("Blank1,VIAL 1,HCYS.m,Blank1,,", file=output)
    print("Blank2,VIAL 1,HCYS.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,HCYS.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,HCYS.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,HCYS.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "Functional Biomarker.m":
            line[2] = "HCYS.m"
        if line[1][1] == "1":
            line[1] = "P1" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P2" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_6_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("hcys6.csv", 'w')
    print(lines[0], end="", file=output)
    print("Blank1,VIAL 1,HCYS.m,Blank1,,", file=output)
    print("Blank2,VIAL 1,HCYS.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,HCYS.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,HCYS.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,HCYS.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "Functional Biomarker.m":
            line[2] = "HCYS.m"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_7_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("hcys7.csv", 'w')
    print(lines[0], end="", file=output)
    print("Blank1,VIAL 1,HCYS.m,Blank1,,", file=output)
    print("Blank2,VIAL 1,HCYS.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,HCYS.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,HCYS.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,HCYS.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "Functional Biomarker.m":
            line[2] = "HCYS.m"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_8_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("hcys8.csv", 'w')
    print(lines[0], end="", file=output)
    print("Blank1,VIAL 1,HCYS.m,Blank1,,", file=output)
    print("Blank2,VIAL 1,HCYS.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,HCYS.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,HCYS.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,HCYS.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "Functional Biomarker.m":
            line[2] = "HCYS.m"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_9_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("hcys9.csv", 'w')
    print(lines[0], end="", file=output)
    print("Blank1,VIAL 1,HCYS.m,Blank1,,", file=output)
    print("Blank2,VIAL 1,HCYS.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,HCYS.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,HCYS.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,HCYS.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "Functional Biomarker.m":
            line[2] = "HCYS.m"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_10_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("hcys10.csv", 'w')
    print(lines[0], end="", file=output)
    print("Blank1,VIAL 1,HCYS.m,Blank1,,", file=output)
    print("Blank2,VIAL 1,HCYS.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,HCYS.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,HCYS.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,HCYS.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "Functional Biomarker.m":
            line[2] = "HCYS.m"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)

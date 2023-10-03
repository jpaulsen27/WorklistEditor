from datetime import date


def acidics_1_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("acidics1_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print("Blank1,VIAL 1,Ultivo Acidics.m,Blank1,,", file=output)
    print("Blank2,VIAL 1,Ultivo Acidics.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Ultivo Acidics.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "ACIDIC.m":
            line[2] = "ULTIVO ACIDICS.m"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def acidics_2_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("acidics2_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print("Blank1,VIAL 1,Ultivo Acidics.m,Blank1,,", file=output)
    print("Blank2,VIAL 1,Ultivo Acidics.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Ultivo Acidics.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "ACIDIC.m":
            line[2] = "ULTIVO ACIDICS.m"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def acidics_3_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("acidics3_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "ACIDIC.m":
            line[2] = "ULTIVO ACIDICS.m"
        if line[1][1] == "1":
            line[1] = "P3" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P4" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def acidics_4_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("acidics4_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "ACIDIC.m":
            line[2] = "ULTIVO ACIDICS.m"
        if line[1][1] == "1":
            line[1] = "P3" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P4" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def acidics_5_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("acidics5_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "ACIDIC.m":
            line[2] = "ULTIVO ACIDICS.m"
        if line[1][1] == "1":
            line[1] = "P5" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P6" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def acidics_6_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("acidics6_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "ACIDIC.m":
            line[2] = "ULTIVO ACIDICS.m"
        if line[1][1] == "1":
            line[1] = "P5" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P6" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def acidics_7_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("acidics7_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "ACIDIC.m":
            line[2] = "ULTIVO ACIDICS.m"
        if line[1][1] == "1":
            line[1] = "P7" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P8" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def acidics_8_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("acidics8_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "ACIDIC.m":
            line[2] = "ULTIVO ACIDICS.m"
        if line[1][1] == "1":
            line[1] = "P7" + line[1][2:5]
        if line[1][1] == "2":
            line[1] = "P8" + line[1][2:5]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def acidics_9_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("acidics9_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "ACIDIC.m":
            line[2] = "ULTIVO ACIDICS.m"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def acidics_10_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("acidics10_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[2] == "ACIDIC.m":
            line[2] = "ULTIVO ACIDICS.m"
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)

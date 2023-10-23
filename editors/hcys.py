from datetime import date


def hcys_1_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("hcys1_" + today_corrected + ".csv", 'w')
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
        if line[3][7:27] == "Functional Biomarker":
            line[3] = line[3][0:6] + "_HCYS_" + line[3][28:44]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def hcys_2_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("hcys2_" + today_corrected + ".csv", 'w')
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
        if line[3][7:27] == "Functional Biomarker":
            line[3] = line[3][0:6] + "_HCYS_" + line[3][28:44]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_3_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("hcys3_" + today_corrected + ".csv", 'w')
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
        if line[3][7:27] == "Functional Biomarker":
            line[3] = line[3][0:6] + "_HCYS_" + line[3][28:44]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_4_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("hcys4_" + today_corrected + ".csv", 'w')
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
        if line[3][7:27] == "Functional Biomarker":
            line[3] = line[3][0:6] + "_HCYS_" + line[3][28:44]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_5_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("hcys5_" + today_corrected + ".csv", 'w')
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
        if line[3][7:27] == "Functional Biomarker":
            line[3] = line[3][0:6] + "_HCYS_" + line[3][28:44]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_6_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("hcys6_" + today_corrected + ".csv", 'w')
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
        if line[3][7:27] == "Functional Biomarker":
            line[3] = line[3][0:6] + "_HCYS_" + line[3][28:44]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_7_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("hcys7_" + today_corrected + ".csv", 'w')
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
        if line[3][7:27] == "Functional Biomarker":
            line[3] = line[3][0:6] + "_HCYS_" + line[3][28:44]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_8_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("hcys8_" + today_corrected + ".csv", 'w')
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
        if line[3][7:27] == "Functional Biomarker":
            line[3] = line[3][0:6] + "_HCYS_" + line[3][28:44]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_9_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("hcys9_" + today_corrected + ".csv", 'w')
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
        if line[3][7:27] == "Functional Biomarker":
            line[3] = line[3][0:6] + "_HCYS_" + line[3][28:44]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def hcys_10_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("hcys10_" + today_corrected + ".csv", 'w')
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
        if line[3][7:27] == "Functional Biomarker":
            line[3] = line[3][0:6] + "_HCYS_" + line[3][28:44]
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)

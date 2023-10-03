from datetime import date


def functional_1_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("functional1_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print("5HR REST,VIAL 1,5HR-REST.M,5HR REST,,", file=output)
    print("Blank2,VIAL 1,Functional Biomarker.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Functional Biomarker.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Functional Biomarker.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,Functional Biomarker.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", file=output)


def functional_2_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("functional2_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print("5HR REST,VIAL 1,5HR-REST.M,5HR REST,,", file=output)
    print("Blank2,VIAL 1,Functional Biomarker.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Functional Biomarker.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Functional Biomarker.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,Functional Biomarker.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", file=output)


def functional_3_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("functional3_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print("5HR REST,VIAL 1,5HR-REST.M,5HR REST,,", file=output)
    print("Blank2,VIAL 1,Functional Biomarker.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Functional Biomarker.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Functional Biomarker.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,Functional Biomarker.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", file=output)


def functional_4_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("functional4_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print("5HR REST,VIAL 1,5HR-REST.M,5HR REST,,", file=output)
    print("Blank2,VIAL 1,Functional Biomarker.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Functional Biomarker.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Functional Biomarker.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,Functional Biomarker.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", file=output)


def functional_5_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("functional5_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print("5HR REST,VIAL 1,5HR-REST.M,5HR REST,,", file=output)
    print("Blank2,VIAL 1,Functional Biomarker.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Functional Biomarker.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Functional Biomarker.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,Functional Biomarker.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", file=output)


def functional_6_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("functional6_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print("5HR REST,VIAL 1,5HR-REST.M,5HR REST,,", file=output)
    print("Blank2,VIAL 1,Functional Biomarker.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Functional Biomarker.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Functional Biomarker.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,Functional Biomarker.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", file=output)


def functional_7_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("functional7_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print("5HR REST,VIAL 1,5HR-REST.M,5HR REST,,", file=output)
    print("Blank2,VIAL 1,Functional Biomarker.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Functional Biomarker.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Functional Biomarker.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,Functional Biomarker.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", file=output)


def functional_8_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("functional8_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print("5HR REST,VIAL 1,5HR-REST.M,5HR REST,,", file=output)
    print("Blank2,VIAL 1,Functional Biomarker.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Functional Biomarker.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Functional Biomarker.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,Functional Biomarker.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", file=output)


def functional_9_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("functional9_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print("5HR REST,VIAL 1,5HR-REST.M,5HR REST,,", file=output)
    print("Blank2,VIAL 1,Functional Biomarker.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Functional Biomarker.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Functional Biomarker.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,Functional Biomarker.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", file=output)


def functional_10_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("functional10_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print("5HR REST,VIAL 1,5HR-REST.M,5HR REST,,", file=output)
    print("Blank2,VIAL 1,Functional Biomarker.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Functional Biomarker.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Functional Biomarker.m,Blank4,,", file=output)
    print("Blank5,VIAL 1,Functional Biomarker.m,Blank5,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", file=output)

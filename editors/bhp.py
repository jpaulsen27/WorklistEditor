from datetime import date


def bhp_1_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("bhp1_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank22,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank33,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_2_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("bhp2_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank22,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank33,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_3_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("bhp3_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank22,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank33,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_4_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("bhp4_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank22,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank33,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_5_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("bhp5_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank22,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank33,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_6_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("bhp6_" + today_corrected + ".csv", 'w')
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
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("bhp7_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank22,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank33,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_8_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("bhp8_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank22,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank33,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_9_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("bhp9_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank22,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank33,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)


def bhp_10_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("bhp10_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,BHP.m,Blank22,,", file=output)
    print("Blank3,VIAL 1,BHP.m,Blank33,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)

def ultivotox_1_build(filename):
    lines = open(filename, 'r').readlines()
    output = open("ultiovotox1.csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,Ultivo Tox.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Ultivo Tox.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Ultivo Tox.m,Blank4,,", file=output)
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
            print("NEG,P2E1,ULTIVO TOX.m,NEG10,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG12,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG6,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG14,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG1,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG3,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG5,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG9,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG11,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG13,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG8,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG16,,", file=output)
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
    print("Blank2,VIAL 1,Ultivo Tox.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Ultivo Tox.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Ultivo Tox.m,Blank4,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG18,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG20,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG22,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG23,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG26,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG28,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG30,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG31,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG17,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG19,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG21,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG25,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG27,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG29,,", file=output)
        if line[0] == "CAL0003POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG24,,", file=output)
        if line[0] == "CAL0004POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG32,,", file=output)
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
    print("Blank2,VIAL 1,Ultivo Tox.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Ultivo Tox.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Ultivo Tox.m,Blank4,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG34,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG36,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG38,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG39,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG42,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG44,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG46,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG47,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG33,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG35,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG37,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG41,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG43,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG45,,", file=output)
        if line[0] == "CAL0005POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG40,,", file=output)
        if line[0] == "CAL0006POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG48,,", file=output)
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
    print("Blank2,VIAL 1,Ultivo Tox.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Ultivo Tox.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Ultivo Tox.m,Blank4,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG50,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG52,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG54,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG55,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG58,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG60,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG62,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG63,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG49,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG51,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG53,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG57,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG59,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG61,,", file=output)
        if line[0] == "CAL0007POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG56,,", file=output)
        if line[0] == "CAL0008POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG64,,", file=output)
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
    print("Blank2,VIAL 1,Ultivo Tox.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Ultivo Tox.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Ultivo Tox.m,Blank4,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG66,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG68,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG70,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG71,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG74,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG76,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG78,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG79,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG65,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG67,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG69,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG73,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG75,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG77,,", file=output)
        if line[0] == "CAL0009POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG72,,", file=output)
        if line[0] == "CAL00010POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG80,,", file=output)
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
    print("Blank2,VIAL 1,Ultivo Tox.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Ultivo Tox.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Ultivo Tox.m,Blank4,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG82,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG84,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG86,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG87,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG90,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG92,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG94,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG95,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG81,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG83,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG85,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG89,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG91,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG93,,", file=output)
        if line[0] == "CAL0011POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG88,,", file=output)
        if line[0] == "CAL0012POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG96,,", file=output)
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
    print("Blank2,VIAL 1,Ultivo Tox.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Ultivo Tox.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Ultivo Tox.m,Blank4,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG98,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG100,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG102,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG103,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG106,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG108,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG110,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG111,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG97,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG99,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG101,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG105,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG107,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG109,,", file=output)
        if line[0] == "CAL0013POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG104,,", file=output)
        if line[0] == "CAL0014POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG112,,", file=output)
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
    print("Blank2,VIAL 1,Ultivo Tox.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Ultivo Tox.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Ultivo Tox.m,Blank4,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG114,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG116,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG118,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG119,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG122,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG124,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG126,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG127,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG113,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG115,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG117,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG121,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG123,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG125,,", file=output)
        if line[0] == "CAL0015POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG120,,", file=output)
        if line[0] == "CAL0016POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG128,,", file=output)
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
    print("Blank2,VIAL 1,Ultivo Tox.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Ultivo Tox.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Ultivo Tox.m,Blank4,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG130,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG132,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG134,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG135,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG138,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG140,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG142,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG143,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG129,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG131,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG133,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG137,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG139,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG141,,", file=output)
        if line[0] == "CAL0017POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG136,,", file=output)
        if line[0] == "CAL0018POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG144,,", file=output)
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
    print("Blank2,VIAL 1,Ultivo Tox.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Ultivo Tox.m,Blank3,,", file=output)
    print("Blank4,VIAL 1,Ultivo Tox.m,Blank4,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG146,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG148,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG150,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG151,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG154,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG156,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG158,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG159,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG145,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,ULTIVO TOX.m,NEG147,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,ULTIVO TOX.m,NEG149,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG153,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,ULTIVO TOX.m,NEG155,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,ULTIVO TOX.m,NEG157,,", file=output)
        if line[0] == "CAL0019POST":
            print("NEG,P1E1,ULTIVO TOX.m,NEG152,,", file=output)
        if line[0] == "CAL0020POST":
            print("NEG,P2E1,ULTIVO TOX.m,NEG160,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)
    print("COLUMNWASH,VIAL 1,COL-1.M,COLUMNWASH1,,", end='', file=output)
    
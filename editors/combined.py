from datetime import date


def combined_1_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("combined1_" + today_corrected + ".csv", 'w')
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
            print("NEG,P2E1,COMBINED.m,NEG10,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG12,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG14,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG9,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG11,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG13,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG15,,", file=output)
        if line[0] == "CAL0001POST":
            print("NEG,P1E1,COMBINED.m,NEG8,,", file=output)
        if line[0] == "CAL0002POST":
            print("NEG,P2E1,COMBINED.m,NEG16,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_2_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("combined2_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG18,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG20,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG22,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG17,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG19,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG21,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG23,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG26,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG28,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG30,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG25,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG27,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG29,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG31,,", file=output)
        if line[0] == "CAL0003POST":
            print("NEG,P1E1,COMBINED.m,NEG24,,", file=output)
        if line[0] == "CAL0004POST":
            print("NEG,P2E1,COMBINED.m,NEG32,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_3_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("combined3_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG34,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG36,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG38,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG33,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG35,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG37,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG39,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG42,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG44,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG46,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG41,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG43,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG45,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG47,,", file=output)
        if line[0] == "CAL0005POST":
            print("NEG,P1E1,COMBINED.m,NEG40,,", file=output)
        if line[0] == "CAL0006POST":
            print("NEG,P2E1,COMBINED.m,NEG48,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_4_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("combined4_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG50,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG52,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG54,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG49,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG51,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG53,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG55,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG58,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG60,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG62,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG57,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG59,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG61,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG63,,", file=output)
        if line[0] == "CAL0007POST":
            print("NEG,P1E1,COMBINED.m,NEG56,,", file=output)
        if line[0] == "CAL0008POST":
            print("NEG,P2E1,COMBINED.m,NEG64,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_5_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("combined5_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG66,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG68,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG70,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG65,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG67,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG69,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG71,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG74,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG76,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG78,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG73,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG75,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG77,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG79,,", file=output)
        if line[0] == "CAL0009POST":
            print("NEG,P1E1,COMBINED.m,NEG72,,", file=output)
        if line[0] == "CAL0010POST":
            print("NEG,P2E1,COMBINED.m,NEG80,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_6_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("combined6_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG82,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG84,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG86,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG81,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG83,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG85,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG87,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG90,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG92,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG94,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG89,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG91,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG93,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG95,,", file=output)
        if line[0] == "CAL0011POST":
            print("NEG,P1E1,COMBINED.m,NEG88,,", file=output)
        if line[0] == "CAL0012POST":
            print("NEG,P2E1,COMBINED.m,NEG96,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_7_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("combined7_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG98,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG100,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG102,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG97,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG99,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG101,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG103,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG106,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG108,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG110,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG105,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG107,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG109,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG111,,", file=output)
        if line[0] == "CAL0013POST":
            print("NEG,P1E1,COMBINED.m,NEG104,,", file=output)
        if line[0] == "CAL0014POST":
            print("NEG,P2E1,COMBINED.m,NEG112,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_8_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("combined8_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG114,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG116,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG118,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG113,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG115,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG117,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG119,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG122,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG124,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG126,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG121,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG123,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG125,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG127,,", file=output)
        if line[0] == "CAL0015POST":
            print("NEG,P1E1,COMBINED.m,NEG120,,", file=output)
        if line[0] == "CAL0016POST":
            print("NEG,P2E1,COMBINED.m,NEG128,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_9_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("combined9_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG130,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG132,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG134,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG129,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG131,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG133,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG135,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG138,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG140,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG142,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG137,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG139,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG141,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG143,,", file=output)
        if line[0] == "CAL0017POST":
            print("NEG,P1E1,COMBINED.m,NEG136,,", file=output)
        if line[0] == "CAL0018POST":
            print("NEG,P2E1,COMBINED.m,NEG144,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)


def combined_10_build(filename):
    today = date.today()
    today_corrected = str(today.strftime('%m%d%y'))
    lines = open("L:\\" + filename, 'r').readlines()
    output = open("combined10_" + today_corrected + ".csv", 'w')
    print(lines[0], end="", file=output)
    print(lines[1], end="", file=output)
    print("Blank2,VIAL 1,Combined.m,Blank2,,", file=output)
    print("Blank3,VIAL 1,Combined.m,Blank3,,", file=output)
    for i in range(2, len(lines)):
        line = lines[i][0:-1].split(',')
        if line[1][1:5] == "1C2":
            print("NEG,P1E1,COMBINED.m,NEG146,,", file=output)
        if line[1][1:5] == "1E2":
            print("NEG,P1E1,COMBINED.m,NEG148,,", file=output)
        if line[1][1:5] == "1G1":
            print("NEG,P1E1,COMBINED.m,NEG150,,", file=output)
        if line[1][1:5] == "1B2":
            print("NEG,P1E1,COMBINED.m,NEG145,,", file=output)
        if line[1][1:5] == "1D2":
            print("NEG,P1E1,COMBINED.m,NEG147,,", file=output)
        if line[1][1:5] == "1F1":
            print("NEG,P1E1,COMBINED.m,NEG149,,", file=output)
        if line[1][1:5] == "1H1":
            print("NEG,P1E1,COMBINED.m,NEG151,,", file=output)
        if line[1][1:5] == "2C2":
            print("NEG,P2E1,COMBINED.m,NEG154,,", file=output)
        if line[1][1:5] == "2E2":
            print("NEG,P2E1,COMBINED.m,NEG156,,", file=output)
        if line[1][1:5] == "2G1":
            print("NEG,P2E1,COMBINED.m,NEG158,,", file=output)
        if line[1][1:5] == "2B2":
            print("NEG,P2E1,COMBINED.m,NEG153,,", file=output)
        if line[1][1:5] == "2D2":
            print("NEG,P2E1,COMBINED.m,NEG155,,", file=output)
        if line[1][1:5] == "2F1":
            print("NEG,P2E1,COMBINED.m,NEG157,,", file=output)
        if line[1][1:5] == "2H1":
            print("NEG,P2E1,COMBINED.m,NEG159,,", file=output)
        if line[0] == "CAL0019POST":
            print("NEG,P1E1,COMBINED.m,NEG152,,", file=output)
        if line[0] == "CAL0020POST":
            print("NEG,P2E1,COMBINED.m,NEG160,,", file=output)
        for n in range(0, len(line)):
            if n == (len(line) - 1):
                print(line[n], file=output)
            else:
                print(line[n], end=',', file=output)

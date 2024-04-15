def Avg():
    filename = input("Enter the file name: ")
    infile = open(filename, 'r')
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        for Xstr in line.split(","):
            total = total + float(Xstr)
            count = count + 1
        line = infile.readline()
    print("The average is",(total/count))
Avg()
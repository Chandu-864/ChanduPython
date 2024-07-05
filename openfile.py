def Avg():
    File_name = input("enter the file name: ")
    infile = open(File_name, 'r')
    Total = 0.0
    Count = 0
    Line = infile.readline()
    while Line != "":
        for Xstr in Line.split(","):
            Total = Total + float(Xstr)
            Count = Count + 1
        Line = infile.readline()
    print("The average is",(Total/Count))
Avg()
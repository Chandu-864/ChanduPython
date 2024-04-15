from math import sqrt

def Getnumbers():
    num = []
    Xstr = input("Enter a enter(or Press ENTER to quit): ")
    while (Xstr != ""):
        X = float(Xstr)
        num.append(X)
        Xstr = input("Enter a enter(or Press ENTER to quit): ")
    print(num)
    return num

def Mean(num):
    total = 0.0
    for numbers in num:
        total = total + numbers
    return (total/len(num))

def Median(num):
    num.sort()
    size = len(num)
    midpos = (size//2)
    if (size % 2 == 0):
        median = ((num[midpos] + num[midpos -1])/2.0)
    else:
        median = num[midpos]
    return median

def StdDev(num,Mean):
    sumdev = 0.0
    for numbers in num:
        dev = Mean - numbers
        sumdev = sumdev + (dev*dev)
    return sqrt((sumdev/(len(num) -1)))

def main():
    print("This program computes Mean, Median, and StandardDeviation")
    data = Getnumbers()
    average = Mean(data)
    median = Median(data)
    deviation = StdDev(data,median)

    print("The mean for the numbers is :",average)
    print("The median for the numbers is :",median)
    print("The standard deviation is: ", deviation)
    
main()
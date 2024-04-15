def main():
    print("This program convertys the date from mm/dd/yy to month day, year format")
    datestr=input("Enter the date in mm/dd/yy: ")
    monthstr,daystr,yearstr=datestr.split("/")
    months=["january","February","march","April","may","june","july","august","september","october","november","december"]
    monthstr=months[int(monthstr)-1]
    print("The converted date is: ",monthstr, daystr+",",yearstr)
main()
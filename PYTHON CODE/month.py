def main():
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = int(input("enter a month(1-12): "))
    pos = (n-1)*3
    monthabbrev = months[pos: pos+3]
    print("The month is ",monthabbrev +".")
main()
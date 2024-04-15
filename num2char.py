def main():
    print("This program coverts the unicodes into characters")
    instring=input("Enter the code that need to be converted: ")
    message=""
    for numstr in instring.split():
        codenum = int(numstr)
        message = message+chr(codenum)
        print("The decoded message is: ",message)
main()
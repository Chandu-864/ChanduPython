def main():
    print("This program gives the computer usernames")
    first=input("enter users first name: ")
    last=input("enter users last name: ")
    username = first[0]+last[:7]
    print("your username is: ",username)
main()
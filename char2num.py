def main():
    print("This program converts textual message into a sequence of numbers representing the unicode encoding of the message")
    message=input("Enter a message that needs to be encoded: ")
    print("Here are the unicode codes")
    for ch in message:
        print(ord(ch),end="")
main()
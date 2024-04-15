from pathlib import Path

def main():
    Name = input("Enter your name: ")
    name = ''

    while Name != '':
        Name = name + Name
        Name = input("Enter your name: ")
        
    content = Path('Filesread/guest.txt')
    content.write_text(Name)
main()
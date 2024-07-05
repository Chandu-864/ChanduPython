from pathlib import Path
import json
print("This code will tell user favorite number based on our database storage")
def store_number():
    User = input("Enter your name: ")
    Number = int(input("Enter your favorite number: "))
    filename = Path('Favorite.json')
    content1 = json.dumps(User)
    content2 = json.dumps(Number)
    filename.write_text(content1)
    filename.write_text(content2)
    print("Hi {User}, we will remember you when you come back")
    return User, Number

def get_number():
    filename = Path('Favorite.json')
    if filename.exists():
        content1 = filename.read_text()
        content2 = filename.read_text()
        user
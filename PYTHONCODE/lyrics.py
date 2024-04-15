def happy():
    return "Happy birthday to you! "
def sing(person):
    lyrics = happy()*2 + "Happy birthday, dear "+ person +". " + happy()
    return lyrics
def main():
    for person in ["chandu", "Padma", "Seenu", "Sushma"]:
        print(sing(person))
main()
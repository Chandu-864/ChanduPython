def happy():
    return "Happy birthday to you "
def thanks():
    print("Thank you")
def sing(person):
    song = happy()*2 + "Happy birthday dear " + person + ". "+ happy()
    return song
def main():
    for person in ["chandu", "Padma", "Seenu", "Sushma"]:
        print(sing(person))
        print()
        thanks()
        print()
main()
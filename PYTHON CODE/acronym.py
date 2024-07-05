def acronym(phrase):
    words = phrase.split(" ")
    result = ""
    for word in words:
        result += word[0].upper()
    return result
phrase = input("Enter a phrase: ")
Acronym = acronym(phrase)
print(Acronym)
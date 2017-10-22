OrigText = input("What message are you sending \n")
words = OrigText.split()
PLtext = []

for word in words:
    firstLetter = word[0]
    if firstLetter.lower() in ["a", "e", "i", "o", "u"]:
        PLword = word + "way"
    else:
        PLword = word[1:] + firstLetter + "ay"
    if word.istitle():
        PLword = PLword.capitalize()
    elif word.isupper():
        PLword = PLword.upper()
    PLtext.append(PLword)

print (" ".join(PLtext))

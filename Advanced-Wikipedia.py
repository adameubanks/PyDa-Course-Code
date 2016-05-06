import wikipedia

while True:
        input = raw_input("Q: ")
        wikipedia.set_lang("es")
        print wikipedia.summary(input, sentences=2)

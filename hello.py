def chatbot():
    name = input("What is your name?")
    first_letter = list(name)
    first_letter[0] = first_letter[0].upper()
    new_word = "".join(first_letter)
    print(f"{new_word}!, you are welcome")
chatbot()    
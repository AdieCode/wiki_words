

def letter_counter(words):
    list_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    list_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for word in words:
        for letter in word:
            if letter.upper() in list_alphabet:
                list_count[list_alphabet.index(letter.upper())] += 1


    for i  in range(26) :
        print(list_alphabet[i] + " : " + str(list_count[i]))

    
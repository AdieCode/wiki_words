def give_letters(list_str):
    print("spliting to list of words ... done")
    new_list = []
    for item in list_str:
        words = item.split(" ")  # Split by space
        for word in words:
            parts = word.split(",")  # Split each word by comma
            for part in parts:
                fragments = part.split(".")  # Split each part by dot
                for fragment in fragments:
                    subparts = fragment.split("(")  # Split each fragment by parentheses
                    for subpart in subparts:
                        subfragments = subpart.split(")")  # Split each subpart by closing parenthesis
                        new_list.extend(subfragments)
    
    print("Writing to file ... done")
    unique_list = set(new_list)

    with open("words.txt", "a", encoding="utf-8") as file:
        for word in unique_list:
            file.write(word.strip("\n")+"\n")
        file.close

def first_letter_capitilized():
    print("Filtering none capitilized letters ... done")
    with open("words.txt", "r", encoding="utf-8") as file:
        words = file.readlines()

    with open("words.txt", "a", encoding="utf-8") as file:
        for word in words:
            if word[0].isupper():
                file.write(word)



with open("info.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    give_letters(lines)

first_letter_capitilized()
print("This is a English to Pig Latin translator")
word_input = input("Enter a word: ")


word_to_list = list(word_input)

first_letter = word_to_list[0]

print(first_letter.upper())

if first_letter.upper() == "A" or first_letter.upper() == "E" or first_letter.upper() == "I" or first_letter.upper() == "O" or first_letter.upper() == "U":
    word_to_list.append("-way")
    pig_latin_word = "".join(word_to_list)
    print("Your word in Pig Latin is: " + pig_latin_word)


else:
    word_to_list.append(first_letter)
    word_to_list.append("-ay")
    del(word_to_list[0])
    pig_latin_word = "".join(word_to_list).lower()
    print("Your word in Pig Latin is: " + pig_latin_word)
def word_flipper(str):
    if len(str) == 0:
        return str

    #split strings into words, as words are separated by spaces so
    words = str.split(" ")
    new_str = ""
    for i in range(len(words)):
        words[i] = words[i][::-1]

    return " ".join(words)

# Test Cases
print ("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print ("Pass" if ('sihT si na elpmaxe' == word_flipper('This is an example')) else "Fail")
print ("Pass" if ('sihT si eno llams pets rof ...' == word_flipper('This is one small step for ...')) else "Fail")

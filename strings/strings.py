"""if the input is the string "water", then the output should be "retaw""""
def string_reverser(str):
    end = len(str) - 1
    reversed = ""
    while (end >= 0):
        reversed += str[end]
        end -= 1

    return reversed

print(string_reverser("abc"))

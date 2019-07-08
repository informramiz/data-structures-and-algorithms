"""if the input is the string "water", then the output should be "retaw"""
def string_reverser(str):
    end = len(str) - 1
    reversed = ""
    while (end >= 0):
        reversed += str[end]
        end -= 1

    return reversed

# Test Cases
print ("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print ("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print ("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")

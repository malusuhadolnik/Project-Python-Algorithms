# Referência bibliográfica: 
# https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/

def is_palindrome_iterative(word):
    if word == "":
        return False

    backwards = ''.join(reversed(word))

    if word == backwards:
        return True
    return False

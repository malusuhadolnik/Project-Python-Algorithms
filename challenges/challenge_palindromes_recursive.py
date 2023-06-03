def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False
    if low_index >= high_index:  # condição base
        return True
    if word[low_index] == word[high_index]:  # itera enquanto forem iguais,
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    return False  # se lowindex diferente de highindex, então não é palíndromo


# is_palindrome_recursive('ANA', 0, 2)

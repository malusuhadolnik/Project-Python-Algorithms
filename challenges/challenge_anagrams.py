# Mergesort: no melhor e pior caso, sua complexidade é de O(n log(n))
# Aqui, a função merge_sort foi implementada como o código da aula do Prof Eli,
# que pode ser encontrado no repositório 025-b-live-lectures/sort/merge_sort.py
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right, array.copy())


def merge(left: list[int], right: list[int], merged: list[int]) -> list[int]:
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged

# Bibliografia consultada:
# https://www.freecodecamp.org/news/python-string-to-array-how-to-convert-text-to-a-list/
# https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python


def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return (first_string, second_string, False)

    # comparação precisa ser case-insensitive. É testado lowercase:
    first_lower = first_string.lower()
    second_lower = second_string.lower()

    first_ordered = merge_sort(list(first_lower))  # output: array de letras
    second_ordered = merge_sort(list(second_lower))

    if "".join(first_ordered) == "".join(second_ordered):
        return ("".join(first_ordered), "".join(second_ordered), True)

    return ("".join(first_ordered), "".join(second_ordered), False)
